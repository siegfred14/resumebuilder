from django.http import request
from django.shortcuts import render, redirect
from .models import Person
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.


def resume(request):
    if request.method == "POST":
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

        person = Person(image=image, name=name, phone=phone, email=email, highschool=highschool, degree=degree,
                        university=university, skill=skill, about_you=about_you, previous_work=previous_work)

        messages.success(request, "Details Uploaded Succesfully")
        person.save()
        return redirect('/')

    return render(request, 'accept.html')

    # return HttpResponse('Please Enter Correct Details', content_type="text/plain")


def pdf(request, id):
    user_profile = Person.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({"user_profile": user_profile})
    pdf = pdfkit.from_string(html, False, option)
    return render(request, "resume.html", {'user_profile': user_profile})
