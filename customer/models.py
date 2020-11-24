from django.db import models
<<<<<<< HEAD
from colorfield.fields import ColorField

class Restaurant(models.Model):
    restaurantSlug = models.SlugField(max_length=50,primary_key=True,default="xyz")
    resName = models.CharField(max_length=200,blank=True)
    active = models.BooleanField(null=True)
    contact = models.CharField(max_length=20,blank=True)
    # first = models.CharField(max_length=10,blank=True)
    # second = models.CharField(max_length=10,blank=True)
    # third = models.CharField(max_length=10,blank=True)
    # fourth = models.CharField(max_length=10,blank=True)
    # fifth = models.CharField(max_length=10,blank=True)
    first = ColorField(default="#FF0000")
    second = ColorField(default="#FF0000")
    third = ColorField(default="#FF0000") 
    fourth = ColorField(default="#FF0000")
    fifth = ColorField(default="#FF0000")
    address = models.TextField(max_length=200,blank=True)
    tagline = models.CharField(max_length=200,blank=True)
    plan = models.CharField(max_length=10,blank=True)
    duration = models.DurationField(null=True)
    cost = models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.resName
class Dish(models.Model):
    restaurantSlug = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dishtype = models.CharField(max_length=200,blank=True)
    dishname = models.CharField(max_length=200,blank=True)
    dishdetails = models.TextField(max_length=500,blank=True)
    cuisine = models.CharField(max_length=200,blank=True)
    dishpic = models.ImageField(max_length=200,blank=True)
    price = models.CharField(max_length=10,blank=True)
    buzzwords = models.TextField(max_length=1000,blank=True)
    def __str__(self):
        return self.dishname
    class Meta:
        verbose_name_plural = "Dishes"
=======

class Restaurant(models.Model):
    name = models.CharField(max_length=200,blank=True) # to store the name of the restaurant
    address = models.CharField(max_length=200,blank=True) # to store the address of the restaurant
    phone_num = models.CharField(max_length=200,blank=True,default="") # to store the contact of the restaurant
    plan = models.CharField(max_length=200,blank=True,default="") # to store plan of the restaurant
    url = models.CharField(max_length=200,blank=True,default="") # to store restaurant website link
    first = models.CharField(max_length=7,blank=True,default="") # to store preference of color
    second = models.CharField(max_length=7,blank=True,default="") # to store preference of color
    third = models.CharField(max_length=200,blank=True,default="") # to store preference of color
    fourth = models.CharField(max_length=200,blank=True,default="") # to store preference of color
    fifth = models.CharField(max_length=200,blank=True,default="") # to store preference of color
    duration = models.DurationField(null=True)
    cost = models.IntegerField(null=True) # to store cost of website
    active = models.BooleanField(null=True) # to store if restaurant is active
    def __str__(self):
        return self.name
class LevelOne(models.Model):
    resid = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dishtype = models.CharField(max_length=200,blank=True)
    dishname = models.CharField(max_length=200,blank=True)
    cuisine = models.CharField(max_length=200,blank=True)
    veg = models.BooleanField(null=True)
    dishpic = models.ImageField(null=True)
    def __init__(self):
        self.dishtype=self.dishtype.title()
        self.dishname=self.dishtype.title()
        self.cuisine=self.dishtype.title()
class LevelTwo(models.Model):
    resid = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    templatename = models.CharField(max_length=200,blank=True)
    timetoCook = models.CharField(max_length=200,blank=True)
    bestseller = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    social1 = models.URLField()
    social2 = models.URLField()
>>>>>>> 994b4b060b99b6a0ad05de867ab28fb03fd8b59e
# Create your models here.