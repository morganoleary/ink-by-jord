from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage

from .forms import ContactForm


def contact(request):

    if request.method == "POST":

        contact_form = ContactForm(
            request.POST,
            request.FILES
        )

        if contact_form.is_valid():

            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            phone = contact_form.cleaned_data["phone"]
            instagram = contact_form.cleaned_data["instagram"]
            placement = contact_form.cleaned_data["placement"]
            description = contact_form.cleaned_data["description"]

            reference_images = request.FILES.getlist(
                "reference_images"
            )

            email_body = f"""
New tattoo enquiry

Name: {name}
Email: {email}
Phone: {phone}
Instagram: {instagram}
Placement & Size: {placement}

Description:
{description}
"""

            enquiry_email = EmailMessage(
                subject=f"New Tattoo Enquiry from {name}",
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )

            for image in reference_images:
                enquiry_email.attach(
                    image.name,
                    image.read(),
                    image.content_type,
                )

            enquiry_email.send()

            messages.success(
                request,
                "Thanks for your enquiry. I'll review your idea and get back to you as soon as possible."
            )

            return redirect("contact")

    else:
        contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        }
    )