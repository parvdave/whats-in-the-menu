<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from . import views

app_name = "customer"

urlpatterns = [
    path('',views.home,name="customer-home"),
    path('register/', views.registerRestaurant,name="restaurant-register"),
    path('add/',views.registerDish,name="add-dishes"),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert,name="hello"),
>>>>>>> 994b4b060b99b6a0ad05de867ab28fb03fd8b59e
]
