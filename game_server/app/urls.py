from django.contrib import admin
from django.urls import path
from . import views
from .views import FrontViewSet

urlpatterns = [
    path('map/', FrontViewSet.as_view({
        'get': 'list',
    })),
]