from django.shortcuts import render
from django.utils import translation


def index(request):
    translation.activate('fa')
    return render(request, 'home/home.html')
