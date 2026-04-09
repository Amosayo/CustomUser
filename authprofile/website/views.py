from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "website/index.html")

def about(request):
    return HttpResponse("<h1> About us page </h1>")

def products(request):
    return HttpResponse("<h1> Products page </h1>")


# Create your views here.
