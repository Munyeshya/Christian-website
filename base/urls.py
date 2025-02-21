from django.urls import path
from base.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('', index, name='index'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
