from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addmap', views.addmap, name='addmap'),
    #path('sendtomaps', views.sendtomaps),
]