from django.urls import path

from . import views

urlpatterns = [
    path("adopt/<int:pet_id>/", views.adopt, name="adopt"),
    path("pet_detail/<int:pet_id>/", views.pet_detail, name="pet_detail"),
    path("pet_search/", views.pet_search, name="pet_search"),
    path("edit_pet/<int:pet_id>/", views.edit_pet, name="edit_pet"),
    path("create_pet/", views.PetCreateView.as_view(), name="create_pet"),
]