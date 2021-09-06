from django.http import request
from django.shortcuts import render
from . import models
from templates import *

# Create your views here.


def resume(request):
    return render(request, 'accept.html')
