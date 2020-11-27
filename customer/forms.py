from django import forms
from .models import Restaurant, Dish
from colorfield.fields import ColorField
from colorful.fields import RGBColorField

class DishForms(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['restaurantSlug','cuisine','dishtype','dishname','dishpic','price','buzzwords','dishdetails']
        labels = {
        "restaurantSlug": "Enter restaurant slug: ",
        "cuisine": "Enter Cuisine",
        'dishtype':"Enter type of dish: ",
        'dishname':"Enter name of dish: ",
        'price':"Enter price of dish: ",
        'dishpic':"Enter picture of dish: ",
        'buzzwords':"Enter buzzwords (example: <b style='color:#00ff00;'>veg</b>,<b style='color:#ff0000;'>non-veg</b>)",
        'dishdetails':"Enter details of the dish: ",
        }
class RestaurantForms(forms.ModelForm):
    first = ColorField(default="#FF0000")
    second = ColorField(default="#FF0000")
    third = ColorField(default="#FF0000") 
    fourth = ColorField(default="#FF0000")
    fifth = ColorField(default="#FF0000")
    class Meta:
        model = Restaurant
        
        labels = {
        "restaurantSlug": "Enter restaurant slug: ",
        "resName":"Enter restaurant name: ",
        "contact" : "Enter contact number: ",
        'first' : "Enter primary color preference: ",
        'second' : "Enter secondary color preference: ",
        'third' : "Enter tertiary color preference: ",
        "fourth":"Enter quarternary color preference: ",
        "fifth":"Enter other color preference: ",
        "address":"Enter restaurant address: ",
        'tagline':"Enter restaurant tagline: ",
        'plan':"Enter plan of choice : ",
        'duration':'Enter duration: ',
        'restaurantImage':'Upload image of restaurant: ',
        'restaurantLogo':'Upload logo of restaurant: ',
        'extraWords':'Enter extra taglines: ',
        }
        fields = ['restaurantSlug','resName','contact','first','second','third','fourth','fifth','address','tagline','plan','duration','cost','restaurantImage','restaurantLogo','extraWords']