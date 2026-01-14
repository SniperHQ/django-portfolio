from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
import logging

from .models import ContactMessage

logger = logging.getLogger(__name__)


def contact_view(request):
    """
    Handles contact form submissions:
    - Validates user input
    - Saves message to database
    - Sends notification email to admin (if configured)
    - Never exposes system errors to users
    """

    contact_info = {
        "email": "hendry91234@gmail.com",
        "phone": "+27636825103",
        "address": "8077 Ext 33, Suncity, Ermelo, 2350, South Africa"
    }

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip() or "Website Inquiry"
        message_text = request.POST.get("message", "").strip()

        # =========================
        # BASIC VALIDATION
        # =========================
        if not name or not email or not message_text:
            messages.error(request, "Please fill in all required fields.")
            return redirect("contact:contact")


        if len(message_text) < 10:
            messages.error(request, "Message is too short.")
            return redirect("contact:contact")


        # =========================
        # SAVE TO DATABASE
        # =========================
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_text,
            created_at=now()
        )

        # =========================
        # EMAIL NOTIFICATION
        # =========================
        admin_email = getattr(settings, "ADMIN_EMAIL", None)

        if admin_email:
            try:
                send_mail(
                    subject=f"New Contact Message: {subject}",
                    message=f"""
New contact message received:

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message_text}
""",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[admin_email],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but NEVER show it to the user
                logger.error(
                    "Contact email failed | Message ID: %s | Error: %s",
                    contact_message.id,
                    str(e)
                )

        messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect("contact:contact")


    return render(request, "contact/contact.html", {
        "contact_info": contact_info
    })
