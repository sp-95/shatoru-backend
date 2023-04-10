from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created


# This function is called when a reset password token is created
@receiver(reset_password_token_created)
def password_reset_token_created(
    sender,
    instance,
    reset_password_token,
    *args,
    **kwargs,
):
    """
    Signal receiver function that sends a password reset email to the user who
    requested the reset.

    Args:
        sender: The sender of the signal.
        instance: The instance that sent the signal.
        reset_password_token: The password reset token that was created.
    """
    # TODO: Move this to a different thread for better performance

    # Create context for the email template
    context = {
        "name": reset_password_token.user.first_name
        or reset_password_token.user.username,
        "customer_portal": "Shatoru",
        "reset_password_token": reset_password_token.key,
    }

    # Render email content for both HTML and plaintext formats
    email_html_message = render_to_string("email/user_reset_password.html", context)
    email_plaintext_message = render_to_string("email/user_reset_password.txt", context)

    # Send an email with the reset password link to the user
    msg = EmailMultiAlternatives(
        subject=f"Password Reset for {context['customer_portal']}",
        body=email_plaintext_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[reset_password_token.user.email],
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
