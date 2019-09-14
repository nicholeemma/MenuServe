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

def manageorders(request):
    content={}
    orders = Order.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "OrderAdd" in request.POST: #checking if there is a request to add a todo
            desk_no = request.POST["desk_no"] #title
            name_of_cuisine = request.POST["name_of_cuisine"] #date
            status = request.POST["status"] #category
            
            time = request.POST["time"] #date
            amount = request.POST["amount"]
            store = request.POST["amount"]
            #content = title + " -- " + date + " " + category #content
            an_order = Order(desk_no=desk_no, name_of_cuisine=name_of_cuisine, 
                                  status=status, time=time,amount=amount,store=store)
            an_order.save() #saving the todo 
            return redirect("/")
        if "OrderDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for order_id in checkedlist:
                delete_order = Order.objects.get(id=int(order_id)) #getting todo id
                delete_order.delete() #deleting todo
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Submitted-Order.html",content)

def managermain(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Manager-Main.html",content)
    
def managerstore(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    stores = Store.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "StoreAdd" in request.POST: #checking if there is a request to add a todo
            location = request.POST["location"] #title
            name = request.POST["name"] #date
            
            #content = title + " -- " + date + " " + category #content
            a_store = Store(name=name, location=location)
            a_store.save() #saving the todo 
            return redirect("/")
    return render(request,"Manager-Store.html",content)
    
def managermanager(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Manager-Manager.html",content)

def manageremployee(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Manager-Employee.html",content)

def managermenu(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Manager-Menu.html",content)
# Create your views here.
