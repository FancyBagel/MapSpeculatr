from django.contrib import admin
from django.urls import path
from . import views
from .views import ServerViewSet

urlpatterns = [
    path('new/<int:map>/<int:player>', ServerViewSet.as_view({
        'get': 'new',
    })),
    path('play/<int:player>', ServerViewSet.as_view({
        'get': 'play',
        'post': 'answer',
    })),
]