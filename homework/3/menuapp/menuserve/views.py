from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Menu, Store, Employee, Manager, Order

def index(request):
    content={}
    # if "register" in request.POST:
    #     return HttpResponseRedirect("/Order")
    
    return render(request,"Menu.html",content)

def home(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Order.html",content)
    

# Create your views here.
