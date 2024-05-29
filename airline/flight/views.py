from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight
# Create your views here.

# creating home page
def home(request):
    return render(request, 'flight/home.html')

# creating form
def form(request):
    return render(request, 'flight/form.html')

# userinput
def insertuser(request):
    FirstName = request.post['first name']
    LastName = request.post['last name']
    x = Flight(FirstName=FirstName,LastName=LastName)
    x.save()
    return render(request, 'flight/home.html')
