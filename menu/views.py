from django.shortcuts import render
from customer.models import Dish, Restaurant
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.

def home(response):
    return render(response,'menu/home.html',{})

def jsonitems(request,cat,slug):
    menuItems = serializers.serialize("json",Dish.objects.all().filter(section=cat,restaurantSlug=slug))
    return JsonResponse(menuItems,safe=False)

def renderTemplate(request,slug):
    res = Restaurant.objects.all().filter(restaurantSlug__iexact=slug).first()
    categories = Dish.objects.values('section').filter(restaurantSlug=slug)
    dishes = Dish.objects.values('dishtype','restaurantSlug').filter(restaurantSlug=slug)
    content = {}
    taglines = res.tagline.split(':')
    extrawords = res.extraWords.split(':')
    menuItems = {}
    categories = set(i.section for i in Dish.objects.all().filter(restaurantSlug=slug))
    for i in range(len(taglines)):
        content.update({taglines[i]:extrawords[i]})
    for i in dishes:
        if i['dishtype'] not in menuItems.keys():
            menuItems.update({i['dishtype']:Dish.objects.all().filter(restaurantSlug=slug,dishtype=i['dishtype'])})
    return render(request,f"menu/Template {res.plan}/index.html",{'categories':categories,'restaurant':res,'menuitems':menuItems.items(),'content':content.items()})

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