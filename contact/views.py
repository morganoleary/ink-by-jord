from django.shortcuts import render, redirect
from django.contrib import messages

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
            reference_image = contact_form.cleaned_data["reference_image"]

            print("----- NEW ENQUIRY -----")
            print("NAME:", name)
            print("EMAIL:", email)
            print("PHONE:", phone)
            print("INSTAGRAM:", instagram)
            print("PLACEMENT & SIZE:", placement)
            print("DESCRIPTION:", description)
            print("REFERENCE IMAGE:", reference_image)
            print("-----------------------")

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