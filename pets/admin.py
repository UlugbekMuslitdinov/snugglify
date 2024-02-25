from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'shelter', 'species', 'breed', 'age', 'photo', 'description', 'is_adopted', 'owner', 'date_added']


admin.site.register(Pet, PetAdmin)