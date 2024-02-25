from django import forms

from .models import Pet


class PetEditForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            "name",
            "species",
            "breed",
            "age",
            "photo",
            "description",
        ]