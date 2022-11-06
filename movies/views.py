from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return HttpResponse("<h1>Welcome to Register Page</h1>")