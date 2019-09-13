from django.db import models
from django.utils import timezone
# Code reference: https://medium.com/fbdevclagos/how-to-build-a-todo-app-with-django-17afdc4a8f8c
# Create your models here.
class Menu(models.Model): 
    name_of_cuisine = models.CharField(max_length=30)
    id_for_dish = models.CharField(max_length=4)
    price = models.IntegerField()
    classification = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

class Order(models.Model):
    desk_no = models.CharField(max_length=4)
    name_of_cuisine = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    time = models.DateField(default = timezone.now().strftime("%d/%m/%y"))
    amount = models.IntegerField()
    # to store: many to one
    store = models.ForeignKey(Store,on_delete=models.CASCADE)

class Store(models.Model):
    # to manager: many to many
    manager = models.ManyToManyField(Manager,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=10)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    # to store: many to many
    store = models.ManyToManyField(Manager)
    
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)

class Manager(models.Model):
    name = models.CharField(max_length=20)



