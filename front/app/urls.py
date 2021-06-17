from django.contrib import admin
from django.urls import path
from . import views
from .views import FrontViewSet

urlpatterns = [
    path('addmap', views.addmap, name='addmap'),
    path('maps', FrontViewSet.as_view({
        'get': 'list',
    })),
    path('play', FrontViewSet.as_view({
        'get': 'play',
    })),
]