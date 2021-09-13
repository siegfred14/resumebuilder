from django.http import request
from django.shortcuts import render
from . import models
from templates import *

# Create your views here.


def resume(request):
    if request.method == "POST":
        person = models.Person
        name = request.POST.get('name')

    return render(request, 'accept.html')
