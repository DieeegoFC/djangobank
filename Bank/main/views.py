from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request
from .forms import CreateNewRequest

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})


def dblist(response):
    ls = Request.objects
    return render(response, 'main/list.html', {'ls': ls})


def create(response): 
    return render(response, 'main/create.html', {'form': CreateNewRequest()})
