from django import forms
from .models import Restaurant, Dish
from colorfield.fields import ColorField

class DishForms(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['restaurantSlug','cuisine','dishtype','dishname','dishpic','price','buzzwords','dishdetails']

class RestaurantForms(forms.ModelForm):
    first = ColorField()
    second = ColorField(default="#FF0000")
    third = ColorField(default="#FF0000") 
    fourth = ColorField(default="#FF0000")
    fifth = ColorField(default="#FF0000")
    class Meta:
        model = Restaurant
        fields = ['restaurantSlug','resName','contact','first','second','third','fourth','fifth','address','tagline','plan','duration','cost','restaurantImage','restaurantLogo','extraWords']