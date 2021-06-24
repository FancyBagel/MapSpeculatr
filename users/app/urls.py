
from django.contrib import admin
from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path('register', UserViewSet.as_view({
        'get': 'register',
    })),
    path('login', UserViewSet.as_view({
        'get': 'login',
    })),
    path('user_list', UserViewSet.as_view({
        'get': 'user_list',
    })),
    path('user_info', UserViewSet.as_view({
        'get': 'user_info',
    })),

]