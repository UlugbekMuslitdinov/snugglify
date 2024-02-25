from django.contrib import admin
from .models import Shelter
from pets.models import Pet
from users.models import Manager


# Register your models here.
class PetInline(admin.TabularInline):
    model = Pet
    extra = 0


class ManagerInline(admin.TabularInline):
    model = Manager
    extra = 0


class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'email', 'website', 'city', 'state', 'zip_code', 'date_added']
    inlines = [PetInline, ManagerInline]


admin.site.register(Shelter, ShelterAdmin)
