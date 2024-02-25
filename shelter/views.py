from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "shelter/index.html")


def why_we_exist(request):
    return render(request, "shelter/why_we_exist.html")
