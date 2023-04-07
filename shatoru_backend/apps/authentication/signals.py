from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender,
    instance,
    reset_password_token,
    *args,
    **kwargs,
):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # TODO: Move this to a different thread
    # create context for the email template
    context = {
        "name": reset_password_token.user.first_name
        or reset_password_token.user.username,
        "customer_portal": "Shatoru",
        "reset_password_token": reset_password_token.key,
    }

    # render email text
    email_html_message = render_to_string("email/user_reset_password.html", context)
    email_plaintext_message = render_to_string("email/user_reset_password.txt", context)

    # send an e-mail to the user
    msg = EmailMultiAlternatives(
        subject=f"Password Reset for {context['customer_portal']}",
        body=email_plaintext_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[reset_password_token.user.email],
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
