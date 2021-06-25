from django.contrib import admin
from django.urls import path
from . import views
from .views import FrontViewSet

app_name='app'
urlpatterns = [
    path('addmap', views.addmap, name='addmap'),
    path('maps', FrontViewSet.as_view({
        'get': 'list',
    }), name='maps'),
    path('play', FrontViewSet.as_view({
        'get': 'play',
    }), name='play'),
    path('send', FrontViewSet.as_view({
        'post': 'send',
    }), name='send'),
    path('new/<int:map>', FrontViewSet.as_view({
        'get': 'new',
    }), name='new'),
    path('main', FrontViewSet.as_view({
        'get': 'index',
    }), name='index'),
    path('confirm', FrontViewSet.as_view({
        'post': 'confirm',
    }), name='confirm'),
    path('login', FrontViewSet.as_view({
        'get': 'login'
    }), name='login'),
    path('verify', FrontViewSet.as_view({
        'post': 'verify'
    }), name='verify'),
    path('register', FrontViewSet.as_view({
        'get': 'register'
    }), name='register'),
    path('verify_register', FrontViewSet.as_view({
        'post': 'verify_register'
    }), name='verify_register'),
    path('logout', FrontViewSet.as_view({
        'get': 'logout'
    }), name='logout'),
]