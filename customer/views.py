from django.shortcuts import render, redirect
from .forms import RestaurantForms,DishForms
from django.contrib import messages
from django.views.generic import TemplateView

app_name = "customer"


def home(response):
    return render(response,'customer/home.html',{})
class RegisterRestaurant(TemplateView):
    def get(self,request):
        form = RestaurantForms()
        return render(request,'customer/register.html',{'form':form})
    def post(self,request):
        form = RestaurantForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('resName')
            messages.success(request,f'{name} has been registered!')
            form.save()
            return redirect("customer:customer-home")
def registerRestaurant(request):
    if request.method == "POST":
        form = RestaurantForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('resName')
            messages.success(request,f'{name} has been registered!')
            form.save()
            return redirect("customer:customer-home")
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
