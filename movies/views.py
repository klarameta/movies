from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
