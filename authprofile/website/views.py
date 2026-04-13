from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/aboutus.html")

def products(request):
    return render(request, "website/products.html")

def learn(request):
    return render(request, "website/learn.html")

def contact(request):
    return render( request, "website/contact.html")


# Create your views here.
