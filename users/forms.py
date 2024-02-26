from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Donation

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "phone", "full_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "phone", "full_name")


class BasicUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["full_name", "email", "phone", "username", "password"]
        labels = {
            "full_name": "Full Name",
            "email": "Email",
            "phone": "Phone",
            "username": "Username",
            "password": "Password",
        }
        help_texts = {
            "username": None,
        }
        widgets = {
            "password": forms.PasswordInput(),
        }


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["amount", "shelter"]
        labels = {
            "amount": "Donation Amount",
            "shelter": "Shelter",
        }
        help_texts = {
            "amount": "Enter the amount you want to donate",
            "shelter": "Select the shelter you want to donate to",
        }
        widgets = {
            "amount": forms.NumberInput(attrs={"step": "0.01"}),
        }