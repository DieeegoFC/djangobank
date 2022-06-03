from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request

# Create your views here.

def index(response):
    output = ''.join(x['curp'] for x in Request.objects.all().values())
    return HttpResponse(output)
