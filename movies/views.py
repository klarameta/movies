from django.shortcuts import render

# Create your views here.

    def about(request):
        return HttpResponse('<h1>Welcome to About Page</h1>')