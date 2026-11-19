from django.contrib import admin
from .models import Foodorder

class FoodorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'fooditem', 'quantity', 'mobno', 'email')

admin.site.register(Foodorder, FoodorderAdmin)
