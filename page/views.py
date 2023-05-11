from django.shortcuts import render
from django.http import HttpResponse
from random import randint


# Create your views here.

def index_view(request):
    context = dict()
    return render(request, "page/index.html", context)

def about_us_view(request):
    context = dict()
    return render(request, 'page/about_us.html', context)

def contact_us_view(request):
    context = dict()
    return render(request, 'page/contact_us.html', context)