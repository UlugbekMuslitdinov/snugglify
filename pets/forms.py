from django import forms
from shelter.default_values import PET_SPECIES, STATES
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


class PetSearchForm(forms.Form):
    species = forms.ChoiceField(choices=[("", "All")] + list(PET_SPECIES))
    state = forms.ChoiceField(choices=[("", "All")] + list(STATES))
    age_min = forms.IntegerField(min_value=0, required=False)
    age_max = forms.IntegerField(min_value=0, required=False)
