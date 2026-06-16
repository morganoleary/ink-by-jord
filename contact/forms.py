from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label="Full Name"
    )

    email = forms.EmailField(
        label="Email Address"
    )

    phone = forms.CharField(
        max_length=30,
        required=False,
        label="Mobile Number"
    )

    instagram = forms.CharField(
        max_length=100,
        required=False,
        label="Instagram Handle"
    )

    placement = forms.CharField(
        max_length=200,
        required=False,
        label="Placement & Approximate Size",
        help_text="e.g. Outer forearm, approximately 15cm x 10cm"
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Describe your tattoo idea, style preferences, and any important details..."
            }
        )
    )

    reference_image = forms.ImageField(
        required=False,
        label="Reference Images"
    )