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
    if response.method == 'POST':
        form = CreateNewRequest(response.POST)
        if form.is_valid():
            t = Request(
                name=form.cleaned_data['name'],
                first_surname=form.cleaned_data['first_surname'],
                second_surname=form.cleaned_data['second_surname'],
                cell_number=form.cleaned_data['cell_number'],
                birthday=form.cleaned_data['birthday'],
                birthplace=form.cleaned_data['birthplace'],
                gender=form.cleaned_data['gender'],
                email=form.cleaned_data['email'],
                card_type=form.cleaned_data['card_type'],
                income=form.cleaned_data['income'],
                curp=form.cleaned_data['curp']
            )
            t.save()
    else:
        form = CreateNewRequest()
    return render(response, 'main/create.html', {'form': form})
