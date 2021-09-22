from django.urls import path
from django.urls.resolvers import URLPattern
from .views import resume

urlpatterns = [
    path('', resume, name="resume"),
]
