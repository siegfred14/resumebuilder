from django.urls import path
from django.urls.resolvers import URLPattern
from .views import resume, pdf, list, resume2
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('resume/', resume, name="resume"),
    path('<int:id>/', pdf, name="pdf"),
    path('list/', list, name="list"),
    path('resume2/', resume2, name='resume2')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()
