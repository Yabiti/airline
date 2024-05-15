
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'flight/home.html')

def form(request):
    return render(request, 'flight/form.html')