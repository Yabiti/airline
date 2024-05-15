from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight
# Create your views here.

def home(request):
    return render(request, 'flight/home.html')

def form(request):
    return render(request, 'flight/form.html')

def insertuser(request):
    FirstName = request.post['fn']
    LastName = request.post['ln']