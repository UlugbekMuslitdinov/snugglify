from django.urls import path

from . import views

urlpatterns = [
    path("why-we-exist/", views.why_we_exist, name="why_we_exist"),
    path("", views.index, name="index"),
]
