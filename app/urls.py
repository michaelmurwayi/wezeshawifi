from django.urls import path, include
from django.contrib import admin
from .views import *
from app import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    
]
