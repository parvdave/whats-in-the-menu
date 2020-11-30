from django.contrib import admin
from django.urls import path,include
from . import views
from .views import RegisterRestaurant

app_name = "customer"

urlpatterns = [
    path('',views.home,name="customer-home"),
    path('register/', RegisterRestaurant.as_view(),name="restaurant-register"),
    path('add/',views.registerDish,name="add-dishes"),
]