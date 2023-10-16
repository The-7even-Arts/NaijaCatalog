from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


def send_confirmation_email(request, user):
    # Generate a token for the user
    token = default_token_generator.make_token(user)
    
    # Encode user ID to include in the confirmation link
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # Build the confirmation link
    current_site = get_current_site(request)
    confirmation_link = f"http://{current_site.domain}/confirm/{uid}/{token}/"

    # Create the email message
    subject = "Activate Your Account"

    message = render_to_string("email/confirmation.html", {
        "user": user,
        "confirmation_link": confirmation_link,
    })

    # Send the email
    send_mail(subject, message, settings.EMAIL_USER, [user.email])