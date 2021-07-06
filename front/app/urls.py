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
    path('map_info/<int:map_id>', FrontViewSet.as_view({
        'get': 'map_info',
    }), name='map_info'),
    path('main', FrontViewSet.as_view({
        'get': 'index',
    }), name='index'),
    path('', FrontViewSet.as_view({
        'get': 'index',
    }), name='blank'),
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
    path('user_info/<int:user_id>', FrontViewSet.as_view({
        'get': 'user_info'
    }), name='user_info'),
]