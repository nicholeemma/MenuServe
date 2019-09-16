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
            store = Store.objects.get(name='Store-A')
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
    managers = Manager.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "StoreAdd" in request.POST: #checking if there is a request to add a todo
            location = request.POST["location"] #title
            name = request.POST["name"] #date
            manager_name = request.POST["manager_select"]
            manager = Manager.objects.get(name=str(manager_name))
            #content = title + " -- " + date + " " + category #content
            a_store = Store(name=name, location=location,store_manager=manager)
            a_store.save() #saving the todo 
            return redirect("/Manager-Store/")
        if "StoreDelete" in request.POST: #checking if there is a request to delete a todo
            d_store_id = request.POST["StoreDelete"] #checked todos to be deleted
            # for todo_id in checkedlist:
            d_store = Store.objects.get(id=d_store_id) #getting todo id
            d_store.delete()
            return redirect("/Manager-Store/")
        if "StoreUpdate" in request.POST: #checking if there is a request to delete a todo
            u_store_id = request.POST["StoreUpdate"]
            u_store_location = request.POST["input_storelocation"] #checked todos to be deleted
            # for todo_id in checkedlist:
            u_store_name = request.POST["input_storename"]
            u_store_manager = request.POST["manager_select"]
            u_store = Store.objects.get(id=u_store_id)
            u_store.location = str(u_store_location)
            u_store.name = str(u_store_name)
            u_store.store_manager  = Manager.objects.get(name=str(u_store_manager))
             #getting todo id
            u_store.save()
            return redirect("/Manager-Store/")
    return render(request,"Manager-Store.html",{"stores":stores,"managers":managers})
    
def managermanager(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    managers = Manager.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "ManagerAdd" in request.POST: #checking if there is a request to add a todo
            gender = request.POST["gender"] #title
            name = request.POST["name"] #date
            
            #content = title + " -- " + date + " " + category #content
            a_manager = Manager(name=name, gender=gender)
            a_manager.save() #saving the todo 
            return redirect("/Manager-Manager/")
        if "ManagerDelete" in request.POST: #checking if there is a request to delete a todo
            d_manager_id = request.POST["ManagerDelete"] #checked todos to be deleted
            # for todo_id in checkedlist:
            d_manager = Manager.objects.get(id=d_manager_id) #getting todo id
            d_manager.delete()
            return redirect("/Manager-Manager/")
        if "ManagerUpdate" in request.POST: #checking if there is a request to delete a todo
            u_manager_id = request.POST["ManagerUpdate"]
            u_manager_gender = request.POST["input_managergender"] #checked todos to be deleted
            # for todo_id in checkedlist:
            u_manager_name = request.POST["input_managername"]
            u_manager = Manager.objects.get(id=u_manager_id)
            u_manager.location = str(u_manager_gender)
            u_manager.name = str(u_manager_name)  #getting todo id
            u_manager.save()
            return redirect("/Manager-Manager/")
    return render(request,"Manager-Manager.html",{"managers":managers})

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
