from django.db import models

from .default_values import STATES


class Shelter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="shelter_logos/")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES, default="AL")
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
