from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            message = contact_form.cleaned_data["message"]

            # For now: just print (later we can email it)
            print(name, email, message)

            messages.success(request, "Your enquiry has been sent successfully!")

            return redirect("contact")

    else:
        contact_form = ContactForm()

    return render(request, "contact/contact.html", {
        "contact_form": contact_form
    })