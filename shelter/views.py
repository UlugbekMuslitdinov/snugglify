from django.shortcuts import render

from users.models import Donation, BasicUser
from pets.models import Pet
from .models import Shelter
from django.db import models


# Create your views here.
def index(request):
    amount_raised = Donation.objects.aggregate(total_donations=models.Sum("amount"))["total_donations"] or 0
    users = BasicUser.objects.all().count()
    adopted_pets = Pet.objects.filter(is_adopted=True).count()
    states = Shelter.objects.values("state").annotate(count=models.Count("state")).count()
    stats = {
        "amount_raised": amount_raised,
        "users": users,
        "adopted_pets": adopted_pets,
        "states": states,
    }
    return render(request, "shelter/index.html", stats)


def why_we_exist(request):
    return render(request, "shelter/why_we_exist.html")


def how_you_can_help(request):
    return render(request, "shelter/how_you_can_help.html")