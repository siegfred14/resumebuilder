from django.http import request
from django.shortcuts import render
from . import models
from templates import *

# Create your views here.


def resume(request):
    if request.method == "POST":
        person = models.Person
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        highschool = request.POST.get('highschool')
        degree = request.POST.get('degree')
        university = request.POST.get('university')
        skill = request.POST.get('skill')
        about_you = request.POST.get('about_you')
        previous_work = request.POST.get('previous_work')

    return render(request, 'accept.html')
