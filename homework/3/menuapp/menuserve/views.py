from django.shortcuts import render,redirect
from .models import Menu, Store, Employee, Manager, Order

def index(request):
    content={}
    return render(request,content)

# Create your views here.
