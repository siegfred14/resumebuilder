from django.http import request
from django.shortcuts import render
from .models import Person
# from templates import *
from django.http import HttpResponse

# Create your views here.


def resume(request):
    if request.method == "POST":
        person = Person(image=image, name=name, phone=phone, email=email, highschool=highschool, degree=degree,
                        university=university, skill=skill, about_you=about_you, previous_work=previous_work)
        image = request.POST.get('image')
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

    # return HttpResponse('Please Enter Correct Details', content_type="text/plain")
