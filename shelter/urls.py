from django.urls import path

from . import views

urlpatterns = [
    path("how-you-can-help/", views.how_you_can_help, name="how_you_can_help"),
    path("why-we-exist/", views.why_we_exist, name="why_we_exist"),
    path("", views.index, name="index"),
]
