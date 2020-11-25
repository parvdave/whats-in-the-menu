from django.db import models
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
    restaurantImage = models.ImageField(null=True)
    restaurantLogo = models.ImageField(null=True)
    extraWords = models.TextField(blank=True,max_length=500)
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
# Create your models here.
