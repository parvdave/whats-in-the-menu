from django.contrib import admin
from django.urls import path
from . import views
from menu import views as menu_views

app_name = "main"

urlpatterns = [
    path('',views.home,name="home"),
    
]
