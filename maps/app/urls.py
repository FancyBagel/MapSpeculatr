from django.contrib import admin
from django.urls import path
from .views import MapViewSet

urlpatterns = [
    path('app', MapViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('locations/<int:id>', MapViewSet.as_view({
        'get': 'locations',
    })),
    path('location/<int:id>/<int:no>', MapViewSet.as_view({
        'get': 'location',
    })),
]