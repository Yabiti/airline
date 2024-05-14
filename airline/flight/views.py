
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'flight/home.html')

def form(request):
    if request.method == "POST":
        form = form(request.POST)
        form = form.save()
    return render(request, 'flight/form.html')