from django.db import models
from django.contrib.auth.models import AbstractUser

from shelter.models import Shelter


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def is_manager(self):
        return hasattr(self, "manager")


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class BasicUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name

