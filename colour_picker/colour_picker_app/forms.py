from django import forms
from .models import Image_Upload

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label = "",
        widget = forms.ClearableFileInput(
            attrs = {
                "class": "form-control", "id": "test"
        })
    )

    class Meta:
        model = Image_Upload
        fields = ("image",)