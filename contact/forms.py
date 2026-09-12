from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):

    MAX_FILES = 5
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB safety limit

    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            "widget",
            MultipleFileInput(
                attrs={
                    "accept": "image/*",
                    "multiple": True,
                }
            )
        )
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):

        if not data:
            return []

        if not isinstance(data, (list, tuple)):
            data = [data]

        if len(data) > self.MAX_FILES:
            raise forms.ValidationError(
                f"Please upload no more than {self.MAX_FILES} reference images."
            )

        cleaned_images = []

        for image in data:

            if image.size > self.MAX_FILE_SIZE:
                raise forms.ValidationError(
                    f"{image.name} is too large. "
                    "Each image must be 5 MB or smaller."
                )

            cleaned_image = forms.ImageField.clean(
                self,
                image,
                initial
            )

            cleaned_images.append(cleaned_image)

        return cleaned_images


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
                "placeholder": (
                    "Describe your tattoo idea, style preferences, "
                    "and any important details..."
                )
            }
        )
    )

    reference_images = MultipleImageField(
        required=False,
        label="Reference Images",
        help_text=(
            "Upload up to 5 images. "
        )
    )