from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
    search_term = request.GET.get("q")
    movies = Movie.objects.all()
    return render(request, "home.html", {"searchTerm": search_term, "movies": movies})


def about(request):
    return render(request, "about.html")


def register(request):
    return HttpResponse("<h1>Welcome to Register Page</h1>")
