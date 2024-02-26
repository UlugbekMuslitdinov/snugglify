from django.shortcuts import render

from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import Shelter, Pet, AdoptionRequest
from users.models import Manager
from .forms import PetEditForm, PetSearchForm


def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    form = PetEditForm(instance=pet)
    if request.method == "POST":
        form = PetEditForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
        return redirect("account_profile")
    return render(request, "pets/edit_pet.html", {"form": form, "pet": pet})


class PetCreateView(CreateView):
    model = Pet
    form_class = PetEditForm
    template_name = "pets/create_pet.html"

    def form_valid(self, form):
        pet = form.save(commit=False)
        manager = Manager.objects.get(user=self.request.user)
        pet.shelter = Shelter.objects.get(manager=manager)
        pet.save()
        return redirect("account_profile")


def pet_search(request):
    form = PetSearchForm(request.GET)
    if form.is_valid():
        species = form.cleaned_data.get("species")
        state = form.cleaned_data.get("state")
        age_min = form.cleaned_data.get("age_min")
        age_max = form.cleaned_data.get("age_max")
        pets = Pet.objects.all()
        if species:
            pets = pets.filter(species=species)
        if state:
            pets = pets.filter(shelter__state=state)
        if age_min:
            pets = pets.filter(age__gte=age_min)
        if age_max:
            pets = pets.filter(age__lte=age_max)
        return render(request, "pets/pet_search.html", {"pets": pets, "form": form})
    return render(request, "pets/pet_search.html", {"form": form})


def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, "pets/pet_detail.html", {"pet": pet})


def adopt(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    adoption_request = AdoptionRequest(pet=pet, adopter=request.user.basicuser)
    adoption_request.save()
    return render(request, "pets/adopt_confirm.html")
