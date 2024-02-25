from django.db import models
from users.models import BasicUser
from shelter.models import Shelter
from shelter.default_values import PET_SPECIES


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    species = models.CharField(max_length=100, choices=PET_SPECIES, default="Dog")
    breed = models.CharField(max_length=100)
    age = models
    photo = models.ImageField(upload_to="pet_photos/")
    description = models.TextField()
    is_adopted = models.BooleanField(default=False)
    owner = models.ForeignKey(BasicUser, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
