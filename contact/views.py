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

            reference_images = request.FILES.getlist(
                "reference_images"
            )

            print("----- NEW ENQUIRY -----")
            print("NAME:", name)
            print("EMAIL:", email)
            print("PHONE:", phone)
            print("INSTAGRAM:", instagram)
            print("PLACEMENT & SIZE:", placement)
            print("DESCRIPTION:", description)

            print("REFERENCE IMAGES:")

            for image in reference_images:
                print(
                    image.name,
                    "-",
                    round(image.size / 1024, 1),
                    "KB"
                )

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