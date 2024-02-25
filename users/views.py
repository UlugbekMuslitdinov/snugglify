from django.shortcuts import render


# Create your views here.
def account_profile(request):
    # check if the user is manager
    # if the user is manager, return the manager profile
    # if the user is not manager, return the basic user profile
    user = request.user
    if user.is_manager():
        manager = user.manager
        shelter = manager.shelter
        pets_in_shelter = shelter.pet_set.all()
        print(manager.user)
        context = {
            "manager": manager,
            "shelter": shelter,
            "pets_in_shelter": pets_in_shelter,
        }
        return render(request, "users/manager_profile.html", context)
    else:
        return render(request, "users/basic_user_profile.html")