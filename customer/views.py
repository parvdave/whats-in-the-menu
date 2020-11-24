<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import RestaurantForms,DishForms
from django.contrib import messages

app_name = "customer"


def home(response):
    return render(response,'customer/home.html',{})
def registerRestaurant(request):
    if request.method == "POST":
        form = RestaurantForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('resName')
            messages.success(request,f'{name} has been registered!')
            form.save()
            return redirect("customer-home")
    else:
        form = RestaurantForms()
    return render(request,'customer/register.html',{'form':form})
def registerDish(request):
    if request.method == "POST":
        form = DishForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('dishname')
            messages.success(request,f'{name} has been added!')
            form.save()
            return redirect("customer:add-dishes")
    else:
        form = DishForms()
    return render(request,'customer/add.html',{'form':form})


# Create your views here.
=======
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,LevelOne,LevelTwo
# Create your views here.
def insert(response):
    if response.method == "POST":
        resname = response.POST.get('restaurant-name')
        resadd = response.POST.get('restaurant-address')
        resplan = response.POST.get('plan')
        rescolor1 = response.POST.get('first')
        rescolor2 = response.POST.get('second')
        rescolor3 = response.POST.get('third')
        rescolor4 = response.POST.get('fourth')
        rescolor5 = response.POST.get('fifth')
        submit = response.POST.get('submit')
        if submit == "Add to DB":
            insertingData = Restaurant(name=resname,address=resadd,phone_num='9619912881',first=rescolor1,second=rescolor2,third=rescolor3,fourth=rescolor4,fifth=rescolor5)
            insertingData.save()
            
        return render(response,'customer/insertdetails.html',{'resname':resname,'resadd':resadd,'resplan':resplan,'rescol1':rescolor1,'submit':submit})
    else:
        return render(response,'customer/insertdetails.html',{})
def login(response):
    return render(response,'customer/reslogin.html',{})
# def register(response):
#     if response.method=="POST":
#         form = Regis
#     return render(response,'customer/register.html',{'form':form})
>>>>>>> 994b4b060b99b6a0ad05de867ab28fb03fd8b59e
