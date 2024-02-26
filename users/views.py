from django.shortcuts import render, redirect
from django.views.generic import CreateView

from users.models import BasicUser, CustomUser, Donation
from pets.forms import PetSearchForm

from .forms import DonationForm
from django.db import models

from django.conf import settings

from pets.models import AdoptionRequest



# Create your views here.
def account_profile(request):
    # check if the user is manager
    # if the user is manager, return the manager profile
    # if the user is not manager, return the basic user profile
    user = request.user
    if user.is_manager():
        manager = user.manager
        shelter = manager.shelter
        pets_in_shelter = shelter.pet_set.all()
        print(manager.user)
        context = {
            "manager": manager,
            "shelter": shelter,
            "pets_in_shelter": pets_in_shelter,
        }
        return render(request, "users/manager_profile.html", context)
    else:
        search_form = PetSearchForm(request.GET)
        pets = user.basicuser.pets_adopted()
        adopted = pets.count()
        donations = user.basicuser.amount_donated()
        shelters_donated = user.basicuser.shelters_donated()
        score = adopted * 5 + donations + shelters_donated * 10
        stats = {
            "adopted": adopted,
            "donations": donations,
            "shelters_donated": shelters_donated,
            "score": score,
        }
        context = {"user": user, "pets": pets, "stats": stats, "search_form": search_form}
        return render(request, "users/basic_user_profile.html", context)


class BasicUserCreateView(CreateView):
    model = CustomUser
    fields = ["full_name", "email", "phone", "username", "password"]
    template_name = "users/signup.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        basic_user = BasicUser(user=user)
        basic_user.save()
        return redirect("login")


def donation_request(request):
    form = DonationForm()
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user.basicuser
            donation.save()
            return redirect("account_profile")
    return render(request, "users/donation_request.html", {"form": form, "stripe_key": settings.STRIPE_TEST_PUBLISHABLE_KEY})


def funds_raised(request):
    manager = request.user.manager
    if manager:
        shelter = manager.shelter
        donations = Donation.objects.filter(shelter=shelter)
        total = donations.aggregate(models.Sum("amount"))["amount__sum"] or 0
        context = {"shelter": shelter, "donations": donations, "total": total}
        return render(request, "users/funds_raised.html", context)
    return redirect("account_profile")


def view_adoptions(request):
    manager = request.user.manager
    if manager:
        shelter = manager.shelter
        adoptions = AdoptionRequest.objects.filter(pet__shelter=shelter)
        context = {"shelter": shelter, "adoptions": adoptions}
        return render(request, "users/view_adoptions.html", context)
    return redirect("account_profile")
