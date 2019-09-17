from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Menu, Store, Employee, Manager, Order

def index(request):
    content={}
    # if "register" in request.POST:
    #     return HttpResponseRedirect("/Order")
    
    return render(request,"Menu.html",content)

def home(request):
    store_=""
    desk_=""
    content={}
    error_message=""
    try:
        
        
        orders = Order.objects.all()
        menus = Menu.objects.all()
        stores = Store.objects.all()
        if request.method == "POST": #checking if the request method is a POST
            if "DeleteOrder" in request.POST:
                d_order = request.POST["DeleteOrder"]
                
                delete_order = Order.objects.get(id=int(d_order)) #getting todo id
                delete_order.delete()
            if "OrderMenu" in request.POST: #checking if there is a request to add a todo
                
                #date
                status = "pending"#category
                menu_id = request.POST["OrderMenu"]
                #time = request.POST["time"] #date
                amount = request.POST["amount"]
                store_ = request.POST["store_select"]
                desk_ = request.POST["desk_no"]
                name_of_cuisine = Menu.objects.get(id = menu_id).name_of_cuisine
                price = Menu.objects.get(id = menu_id).price
                store = Store.objects.get(name=str(store_))
                time = "2019-09-17"
                #content = title + " -- " + date + " " + category #content
                an_order = Order(desk_no=desk_, name_of_cuisine=name_of_cuisine, time=time,
                                    status=status, amount=amount, store=store ,price=price)
                an_order.save() #saving the todo 
                return redirect("/Order/")
            if "OrderDelete" in request.POST: #checking if there is a request to delete a todo
                checkedlist = request.POST["checkedbox"] #checked todos to be deleted
                for order_id in checkedlist:
                    delete_order = Order.objects.get(id=int(order_id)) #getting todo id
                    delete_order.delete() #deleting todo
    except:
        content["show"]="Error! check your input"
        error_message = content["show"]
        return render(request,"Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 


    
    return render(request,"Order.html",{"stores":stores,"orders":orders,"menus":menus,"show":error_message})

def manageorders(request):
    content={}
    try:
        orders = Order.objects.all()
        menus = Menu.objects.all()
        stores = Store.objects.all()
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
            if "OrderUpdate" in request.POST: #checking if there is a request to delete a todo
                u_id = request.POST["OrderUpdate"]
                u_input_desk_no = request.POST["input_desk_no"]
                u_cuisine_select = request.POST["cuisine_select"] #checked todos to be deleted
                # for todo_id in checkedlist:
                u_input_amount = request.POST["input_amount"]
                u_input_status = request.POST["input_status"]
                #u_input_time = request.POST["input_time"]
                u_input_status = request.POST["input_price"]
                u_input_store = request.POST["store_select"]
                u_order = Order.objects.get(id = u_id)
                u_order.desk_no = str(u_input_desk_no)
                u_order.name_of_cuisine = str(u_cuisine_select)
                u_order.amount = str(u_input_amount)
                u_order.status = u_input_status
                #u_order.time = u_input_time
                u_order.store = Store.objects.get(name = str(u_input_store ))
                    
                u_order.save()
                return redirect("/Submitted-Order/")
            if "DeleteUpdate" in request.POST: #checking if there is a request to delete a todo
                d_order = request.POST["DeleteUpdate"] #checked todos to be deleted
                
                delete_order = Order.objects.get(id=int(d_order)) #getting todo id
                delete_order.delete() #deleting todo
                return redirect("/Submitted-Order/")
    except:
        content["show"]="Error! check your input"
        error_message = content["show"]
        return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 

#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus})

def managermain(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    return render(request,"Manager-Main.html",content)
    
def managerstore(request):
    content={}
    content["show"]=""
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    try:
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
    except:
        content["show"]="Error! check your input"
        error_message = content["show"]
        return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
    return render(request,"Manager-Store.html",{"stores":stores,"managers":managers})
    
def managermanager(request):
    content={}
    content["show"]=""
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    try:
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
    except:
        content["show"]="Error! check your input"
        error_message = content["show"]
        return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
    return render(request,"Manager-Manager.html",{"managers":managers})

def manageremployee(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    
    content["show"]=""
    store_message=""
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    try:
        stores = Store.objects.all()
        managers = Manager.objects.all()
        employees = Employee.objects.all()
        if request.method == "POST": #checking if the request method is a POST
            if "EmployeeAdd" in request.POST: #checking if there is a request to add a todo
                 #title
                name = request.POST["name"] #date
                manager_name = request.POST["manager_select"]
                manager = Manager.objects.get(name=str(manager_name))
                store_name = request.POST["store_select"]
                store = Store.objects.get(name=str(store_name))
                #content = title + " -- " + date + " " + category #content
                # flst = FollowerList.objects.create(follower=user)
                # flst.followed.add(user)
                a_employee = Employee.objects.create(name=name,manager=manager)
                a_employee.e_store.add(store)
                a_employee.save() #saving the todo 
                for s in a_employee.e_store.all():
                    store_message+=str(s.name)
                
                content["show"]=store_message
                
                #getting todo id
                return redirect("/Manager-Employee/")
            if "EmployeeDelete" in request.POST: #checking if there is a request to delete a todo
                d_Employee_id = request.POST["EmployeeDelete"] #checked todos to be deleted
                # for todo_id in checkedlist:
                d_Employee = Employee.objects.get(id=d_Employee_id) #getting todo id
                d_Employee.delete()
                return redirect("/Manager-Employee/")
            if "EmployeeUpdate" in request.POST: #checking if there is a request to delete a todo
                u_employee_id = request.POST["EmployeeUpdate"]
                 #checked todos to be deleted
                # for todo_id in checkedlist:
                u_employee_name = request.POST["input_employeename"]
                u_employee_manager = request.POST["manager_select"]
                u_employee = Employee.objects.get(id=u_employee_id)
                #u_employee_store = request.POST["store_select"]
                u_employee.name = str(u_employee_name)
                u_employee.manager  = Manager.objects.get(name=str(u_employee_manager))
                #u_employee.e_store.add(Store.objects.get(name=str(u_employee_store)))
                
                # for s in u_employee.e_store.all():
                #     store_message.append(s.name+" ")
                
                # content["show"]=store_message
                # store_message=content["show"]
                for s in u_employee.e_store.all():
                    store_message.append(s.name+" ")
                
                content["show"]=store_message
                store_message=content["show"]
                #getting todo id
                #getting todo id
                u_employee.save()
                return redirect("/Manager-Employee/")
            if "EmployeeAddStore" in request.POST:
                u_employee_store = request.POST["store_select"]
                u_employee_name = request.POST["employee_select"]
                u_employee = Employee.objects.get(name=u_employee_name)
                u_employee.e_store.add(Store.objects.get(name=str(u_employee_store)))
                u_employee.save()
                for s in u_employee.e_store.all():
                    store_message.append(s.name+" ")
                
                content["show"]=store_message
                
                #getting todo id
                return redirect("/Manager-Employee/")
    except:
        content["show"]="Error! check your input"
        error_message = content["show"]
        return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show":error_message,"employees":employees}) 
    return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"employees":employees, "show":store_message})


    

def managermenu(request):
    content={}
#     if "register" in request.POST:
#         return HttpResponseRedirect("/Order")
    menus = Menu.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "MenuAdd" in request.POST: #checking if there is a request to add a todo
            id_for_dish = request.POST["id_for_dish"] #title
            name_of_cuisine = request.POST["name_of_cuisine"] #date
            price = request.POST['price']
            category = request.POST['menu_select']
            description = request.POST['description']
            #content = title + " -- " + date + " " + category #content
            a_menu = Menu(id_for_dish=id_for_dish, name_of_cuisine=name_of_cuisine,price=price,classification=category,description=description)
            a_menu.save() #saving the todo 
            return redirect("/Manager-Menu/")
        if "MenuDelete" in request.POST: #checking if there is a request to delete a todo
            d_Menu_id = request.POST["MenuDelete"] #checked todos to be deleted
            # for todo_id in checkedlist:
            d_menu = Menu.objects.get(id=d_Menu_id) #getting todo id
            d_menu.delete()
            return redirect("/Manager-Menu/")
        if "MenuUpdate" in request.POST: #checking if there is a request to delete a todo
            u_Menu_id = request.POST["MenuUpdate"]
            u_Menu_id_dish = request.POST["input_menuid_for_dish"] #checked todos to be deleted
            # for todo_id in checkedlist:
            u_menu_name = request.POST["input_menuname_of_cuisine"]
            u_category = request.POST['menu_select']
            u_description = request.POST['input_menudescription']
            u_price = request.POST['input_menuprice']
            u_menu = Menu.objects.get(id=u_Menu_id)
            u_menu.id_for_dish = str(u_Menu_id_dish)
            u_menu.name_of_cuisine = str(u_menu_name)
            u_menu.classification = str(u_category)
            u_menu.description = str(u_description) 
            u_menu.price = str(u_price)  #getting todo id
            u_menu.save()
            return redirect("/Manager-Menu/")
    return render(request,"Manager-Menu.html",{"menus":menus})
# Create your views here.
