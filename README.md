# Ex02 Django ORM Web Application
# Date: 19-11-2026
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM

**admin.py**
```python
from django.contrib import admin
from .models import Foodorder

class FoodorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'fooditem', 'quantity', 'mobno', 'email')

admin.site.register(Foodorder, FoodorderAdmin)
```

**models.py**
```python
from django.db import models

class Foodorder(models.Model):
    name = models.CharField(max_length=100)
    fooditem = models.CharField(max_length=100)
    quantity = models.IntegerField()
    mobno = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
```
**urls.py**
```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
# OUTPUT
<img width="1912" height="908" alt="image" src="https://github.com/user-attachments/assets/cbc858c9-e54d-4694-ab14-ae913de92049" />


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
