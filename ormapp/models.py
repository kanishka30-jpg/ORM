from django.db import models

from django.db import models

class Foodorder(models.Model):
    name = models.CharField(max_length=100)
    fooditem = models.CharField(max_length=100)
    quantity = models.IntegerField()
    mobno = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
