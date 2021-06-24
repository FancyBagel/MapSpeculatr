from django.contrib import admin
from django.urls import path
from . import views
from .views import FrontViewSet

app_name='app'
urlpatterns = [
    path('addmap', views.addmap, name='addmap'),
    path('maps', FrontViewSet.as_view({
        'get': 'list',
    })),
    path('play', FrontViewSet.as_view({
        'get': 'play',
    })),
    path('send', FrontViewSet.as_view({
        'post': 'send',
    })),
    path('new/<int:map>', FrontViewSet.as_view({
        'get': 'new',
    })),
    path('', FrontViewSet.as_view({
        'get': 'index',
    })),
    path('confirm', FrontViewSet.as_view({
        'post': 'confirm',
    })),
    path('login', FrontViewSet.as_view({
        'get': 'login'
    })),
    path('verify', FrontViewSet.as_view({
        'post': 'verify'
    }), name='verify'),
    path('logout', FrontViewSet.as_view({
        'get': 'logout'
    })),
]