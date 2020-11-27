from django.shortcuts import render
from customer.models import Dish, Restaurant
# Create your views here.

def home(response):
    return render(response,'menu/home.html',{})

def renderTemplate(request,slug):
    res = Restaurant.objects.values('restaurantSlug','resName','plan','tagline','extraWords').filter(restaurantSlug__iexact='Nomnom')[0]
    dishes = Dish.objects.values('dishtype','restaurantSlug').filter(restaurantSlug=slug)
    content = {}
    taglines = res['tagline'].split(':')
    extrawords = res['extraWords'].split(':')
    menuItems = {}
    for i in range(len(taglines)):
        content.update({taglines[i]:extrawords[i]})
    
    for i in dishes:
        if i['dishtype'] not in menuItems.keys():
            menuItems.update({i['dishtype']:Dish.objects.all().filter(restaurantSlug=slug.title(),dishtype=i['dishtype'])})
    return render(request,f"menu/Template {res['plan']}/index.html",{'restaurant':res,'menuitems':menuItems.items(),'content':content.items()})

def renderTemplate5(request,slug):
    res = Restaurant.objects.values('restaurantSlug','resName').filter(restaurantSlug__iexact=slug)[0]
    dishtypes = Dish.objects.values('dishtype','restaurantSlug','buzzwords','cuisine','dishname','price').filter(restaurantSlug=slug)
    bestseller = []
    menuItems = {}
    for i in dishtypes:
        if i['dishtype'] not in menuItems.keys():
            menuItems.update({i['dishtype']:Dish.objects.all().filter(restaurantSlug=slug,dishtype=i['dishtype'])})
    dishes = Dish.objects.values('dishname','buzzwords','cuisine','dishtype','dishpic','price').filter(restaurantSlug=slug)
    for i in range(len(dishes)):
        if 'bestseller' in dishes[i]['buzzwords']:
            bestseller.append(dishes[i])
        bestseller[i]['buzzwords']=bestseller[i]['buzzwords'].split() 
    return render(request,'menu/Template 5/final.html',{'restaurant':res,'menuitems':menuItems.items(),'bestsellers':bestseller})