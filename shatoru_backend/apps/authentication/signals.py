from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):

    # TODO: Move this to a different thread
    # TODO: Use an email template
    email_plaintext_message = (
        "A Password Reset for the Shatoru App was requested using your email id. "
        "If it wasn't you then you can ignore this email.\n\n"
        "Use the token below in your mobile app to reset your password:\n"
        f"Token: {reset_password_token.key}\n"
        "\nBest Regards,\n"
        "Shatoru Admin\n"
    )

    send_mail(
        subject="Password Reset for Shatoru",
        message=email_plaintext_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[reset_password_token.user.email],
    )
