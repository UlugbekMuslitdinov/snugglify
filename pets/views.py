from django.shortcuts import render

from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import Shelter, Pet
from users.models import Manager
from .forms import PetEditForm


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