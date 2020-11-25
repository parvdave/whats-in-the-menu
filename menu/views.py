from django.shortcuts import render
from customer.models import Dish, Restaurant
# Create your views here.

def home(response):
    return render(response,'menu/home.html',{})

def renderTemplate(request,slug):
    restaurant = Restaurant.objects.all().filter(restaurantSlug=slug.title())[0]
    dishes = Dish.objects.values('dishtype','restaurantSlug').filter(restaurantSlug=slug.title())
    menuItems = {}
    for i in dishes:
        if i['dishtype'] not in menuItems.keys():
            menuItems.update({i['dishtype']:Dish.objects.all().filter(restaurantSlug=slug.title(),dishtype=i['dishtype'])})
    return render(request,'menu/index.html',{'restaurant':restaurant,'menuitems':menuItems.items()})

def template5(request):
    return render(request,'menu/template5.html',{})