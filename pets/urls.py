from django.urls import path

from . import views

urlpatterns = [
    path("edit_pet/<int:pet_id>/", views.edit_pet, name="edit_pet"),
    path("create_pet/", views.PetCreateView.as_view(), name="create_pet"),
]