
# The order of classes matters, the below class will be based on the above ones

from django.db import models
from django.utils import timezone
import datetime
# Code reference: https://medium.com/fbdevclagos/how-to-build-a-todo-app-with-django-17afdc4a8f8c


class Menu(models.Model): 
    
    name_of_cuisine = models.CharField(max_length=30)
    id_for_dish = models.CharField(max_length=4)
    price = models.IntegerField()
    classification = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

class Manager(models.Model):

    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20,default='male')

class Store(models.Model):
       
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    store_manager = models.ForeignKey(Manager,on_delete=models.CASCADE)


    

class Order(models.Model):

    desk_no = models.CharField(max_length=4)
    name_of_cuisine = models.CharField(max_length=30)
    status = models.CharField(max_length=10,default='pending')
    time = models.DateField(default = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
    amount = models.IntegerField()
    price = models.IntegerField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    class Meta:
        ordering = ["-time"]
    def __str__(self):
        return self.name_of_cuisine

class Employee(models.Model):
    name = models.CharField(max_length=20)
    e_store = models.ManyToManyField(Store)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)




