# from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# from django.urls import reverse


# Create your views here.
def index(request):
    # Handle the case where is the user not authenticated: show them the landing page.
    if not request.user.is_authenticated:
        return render(request, "home/index.html")

    return render(request, "home/home.html")
