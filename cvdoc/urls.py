from django.urls import path
from django.urls.resolvers import URLPattern
from .views import resume, pdf, list
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', resume, name="resume"),
    path('<int:id>/', pdf, name="pdf"),
    path('list/', list, name="list")
]
urlpatterns += staticfiles_urlpatterns()
