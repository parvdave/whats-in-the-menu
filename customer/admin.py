from django.contrib import admin
<<<<<<< HEAD
from .models import Restaurant,Dish

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)

=======
from  .models import Restaurant, LevelOne, LevelTwo
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(LevelOne)
admin.site.register(LevelTwo)
>>>>>>> 994b4b060b99b6a0ad05de867ab28fb03fd8b59e
