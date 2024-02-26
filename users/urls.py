from django.urls import path

from . import views

urlpatterns = [
    path("funds-raised/", views.funds_raised, name="funds_raised"),
    path("donation/", views.donation_request, name="donation_request"),
    path("signup/", views.BasicUserCreateView.as_view(), name="signup"),
    path("", views.account_profile, name="account_profile"),
]