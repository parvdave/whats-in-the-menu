from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "customer"

urlpatterns = [
    path('',views.home,name="customer-home"),
    path('register/', views.registerRestaurant,name="restaurant-register"),
    path('add/',views.registerDish,name="add-dishes"),
]