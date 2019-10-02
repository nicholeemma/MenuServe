from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Menu, Store, Employee, Manager, Order,Document
from django.core.files.storage import FileSystemStorage
def index(request):
    '''
    Function for main page
    '''
    
    content={}
    error_message=""
    menus = Menu.objects.all()
    if request.method == "POST":
        if "search" in request.POST:
            try:
                name = request.POST["searchcontent"]
                if name=="":
                    menus = Menu.objects.all()
                else:
                    menus = Menu.objects.filter(name_of_cuisine=name)
            except:
                content["show"]="What you deleted does not exist"
                error_message = content["show"]
                return render(request,"Menu.html",{"menus":menus,"show":error_message})
        if "select" in request.POST:
            menus = ""
            try:
                # getlist method is important to remember
                checkedlist = request.POST.getlist('checkedbox')
                #checkedlist = request.POST["checkedbox"] 
                for checked_classification in checkedlist:
                    
                    menus = Menu.objects.filter(classification=checked_classification)
                   
            except:
                content["show"]="What you deleted does not exist"
                error_message = content["show"]
                return render(request,"Menu.html",{"menus":menus,"show":error_message})
    
    
    return render(request,"Menu.html",{"menus":menus})


def home(request):
    '''
    Function for order page
    '''
    store_=""
    desk_=""
    content={}
    error_message=""
    
        
        
    orders = Order.objects.all()
    menus = Menu.objects.all()
    stores = Store.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        #checking if there is a request to delete an order
        if "DeleteOrder" in request.POST:
            try:
                d_order = request.POST["DeleteOrder"]
                
                delete_order = Order.objects.get(id=int(d_order)) 
                delete_order.delete()
            except:
                content["show"]="What you deleted does not exist"
                error_message = content["show"]
                return render(request,"Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 

        #checking if there is a request to add an order
        if "OrderMenu" in request.POST: 
            
            
            status = "pending"
            menu_id = request.POST["OrderMenu"]
            #time = request.POST["time"] #date
            try:
                amount = int(request.POST["amount"])
            except:
                content["show"]="Amount must be integer"
                error_message = content["show"]
                return render(request,"Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            store_ = request.POST["store_select"]
            desk_ = request.POST["desk_no"]
            name_of_cuisine = Menu.objects.get(id = menu_id).name_of_cuisine
            price = Menu.objects.get(id = menu_id).price * amount
            try:
                store = Store.objects.get(name=str(store_))
            except:
                content["show"]="Store does not exist"
                error_message = content["show"]
                return render(request,"Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            time = "2019-09-21"
            
            try:
                an_order = Order(desk_no=desk_, name_of_cuisine=name_of_cuisine, time=time,
                                    status=status, amount=amount, store=store ,price=price)
                an_order.save() #saving 
            except:
                content["show"]="Input does not comply with rules. Check your input"
                error_message = content["show"]
                return render(request,"Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            return redirect("/Order/")    
    return render(request,"Order.html",{"stores":stores,"orders":orders,"menus":menus,"show":error_message})

def manageorders(request):
    '''
    Function for sumbit-order page
    '''
    content={}
    
    orders = Order.objects.all()
    menus = Menu.objects.all()
    stores = Store.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        
        if "OrderUpdate" in request.POST: #checking if there is a request to delete a todo
            u_id = request.POST["OrderUpdate"]
            u_input_desk_no = request.POST["input_desk_no"]
            u_cuisine_select = request.POST["cuisine_select"] 
            
            u_input_amount = request.POST["input_amount"]
            u_input_status = request.POST["input_status"]
            #u_input_time = request.POST["input_time"]
            
            u_input_store = request.POST["store_select"]
            try:
                u_order = Order.objects.get(id = u_id)
            except:
                content["show"]="order does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message})
            try:    
                u_order.desk_no = str(u_input_desk_no)
                u_order.name_of_cuisine = str(u_cuisine_select)
                u_order.status = u_input_status
            except:
                content["show"]="Input exceeds the allowed length"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message})
            try:
                u_order.amount = int(u_input_amount)
            except:
                content["show"]="amount should be integer"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            try:
                u_order.price = int(int(Menu.objects.get(name_of_cuisine = u_cuisine_select).price)*int(u_input_amount))
            except:
                content["show"]="menu does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message})               
            #u_order.time = u_input_time
            try:
                u_order.store = Store.objects.get(name = str(u_input_store ))
            except:
                content["show"]="Store does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            try:

                u_order.save()
            except:
                content["show"]="input does not comply with rules, check input"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            
            return redirect("/Submitted-Order/")
        if "DeleteUpdate" in request.POST: #checking if there is a request to delete a todo
            d_order = request.POST["DeleteUpdate"] #checked todos to be deleted
            try:
                delete_order = Order.objects.get(id=int(d_order)) #getting todo id
            except:
                content["show"]="Order does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 

            delete_order.delete() #deleting todo
            return redirect("/Submitted-Order/")

    return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus})

def managermain(request):
    '''
    Function for manager-main page
    '''
    content={}

    return render(request,"Manager-Main.html",content)
    
def managerstore(request):
    content={}
    # for display error message 
    content["show"]=""

    
    stores = Store.objects.all()
    managers = Manager.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "StoreAdd" in request.POST: 
            location = request.POST["location"] 
            name = request.POST["name"] 
            manager_name = request.POST["manager_select"]
            try:
                manager = Manager.objects.get(name=str(manager_name))
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            try:
                a_store = Store(name=name, location=location,store_manager=manager)
                a_store.save() 
            except:
                content["show"]="Add cannot be done, check your input"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            return redirect("/Manager-Store/")
        if "StoreDelete" in request.POST: #checking if there is a request to delete a todo
            d_store_id = request.POST["StoreDelete"] #checked todos to be deleted
            # for todo_id in checkedlist:
            try:
                d_store = Store.objects.get(id=d_store_id) #getting todo id
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            d_store.delete()
            return redirect("/Manager-Store/")
        if "StoreUpdate" in request.POST: 
            try:
                u_store_id = request.POST["StoreUpdate"]
                u_store_location = request.POST["input_storelocation"]            
                u_store_name = request.POST["input_storename"]
                u_store_manager = request.POST["manager_select"]
                u_store = Store.objects.get(id=u_store_id)
                u_store.location = str(u_store_location)
                u_store.name = str(u_store_name)
            except:
                content["show"]="update cannot be done, check your input"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            try:
                u_store.store_manager  = Manager.objects.get(name=str(u_store_manager))
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            try:
                u_store.save()
            except:
                content["show"]="update cannot be done, check your input"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message})
            return redirect("/Manager-Store/")

    return render(request,"Manager-Store.html",{"stores":stores,"managers":managers})
    
def managermanager(request):
    '''
    Function for manage managers'''
    content={}
    # for display error message 
    content["show"]=""

    
    managers = Manager.objects.all()
    if request.method == "POST": 
        if "ManagerAdd" in request.POST: 
            gender = request.POST["gender"] 
            name = request.POST["name"] 
            try:
                a_manager = Manager(name=name, gender=gender)
                a_manager.save() 
            except:
                content["show"]="Add cannot be done, check your input"
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
            return redirect("/Manager-Manager/")
        if "ManagerDelete" in request.POST: #checking if there is a request to delete a todo
            d_manager_id = request.POST["ManagerDelete"] #checked todos to be deleted
            try:
                d_manager = Manager.objects.get(id=d_manager_id) #getting todo id
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
            d_manager.delete()
            return redirect("/Manager-Manager/")
        if "ManagerUpdate" in request.POST: #checking if there is a request to delete a todo
            u_manager_id = request.POST["ManagerUpdate"]
            u_manager_gender = request.POST["input_managergender"] #checked todos to be deleted
            # for todo_id in checkedlist:
            u_manager_name = request.POST["input_managername"]
            try:
                u_manager = Manager.objects.get(id=u_manager_id)
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
            u_manager.location = str(u_manager_gender)
            u_manager.name = str(u_manager_name)  #getting todo id
            try:
                u_manager.save()
            except:
                content["show"]="Check your input"
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message})
            return redirect("/Manager-Manager/")

    
    return render(request,"Manager-Manager.html",{"managers":managers})

def manageremployee(request):
    '''
    Functions for manage employee page
    '''
    content={}

    # for display error message 
    content["show"]=""
    content["show_error"]=""
    store_message=""

    
    stores = Store.objects.all()
    managers = Manager.objects.all()
    employees = Employee.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "search" in request.POST:
            try:
                name = request.POST["searchcontent"]
                if name=="":
                    employees = Employee.objects.all()
                else:
                    employees = Employee.objects.filter(name=name)
            except:
                content["show_error"]="Employee does not exist?"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees}) 
   
# This select function will be realized in the future   
        # if "store-selct" in request.POST:
        #     selected_store = request.POST["selectedstore"]
        #     #employees = Employee.e_store_set.filter(e_store__contains=selected_store).distinct()
        #     # a = Store.objects.get(id=selected_store )
        #     # employees = a.employee_set.all()
        #     e = Store.objects.get(id=selected_store)
        #     employees = e.employees.all()
        if "EmployeeAdd" in request.POST:
               
            name = request.POST["name"] 
            manager_name = request.POST["manager_select"]
            try:
                manager = Manager.objects.get(name=str(manager_name))
            except:                
                content["show"]="manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show":error_message,"employees":employees}) 
            
            store_name = request.POST["store_select"]
            try:
                store = Store.objects.get(name=str(store_name))
            except:
                
                content["show_error"]="Store does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees}) 
            try:
                a_employee = Employee.objects.create(name=name,manager=manager)
                a_employee.e_store.add(store)
                a_employee.save() 
            except:
                content["show_error"]="Add cannot be done, check your input"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees}) 
            for s in a_employee.e_store.all():
                store_message+=str(s.name)
            
            content["show"]=store_message
            
            #getting todo id
            return redirect("/Manager-Employee/")
        if "EmployeeDelete" in request.POST: #checking if there is a request to delete a todo
            d_Employee_id = request.POST["EmployeeDelete"] #checked todos to be deleted
            try:
                d_Employee = Employee.objects.get(id=d_Employee_id)
            except:
                content["show_error"]="Store does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            d_Employee.delete()
            return redirect("/Manager-Employee/")
        if "EmployeeUpdate" in request.POST: 
            u_employee_id = request.POST["EmployeeUpdate"]
            u_employee_name = request.POST["input_employeename"]
            u_employee_manager = request.POST["manager_select"]
            try:
                u_employee = Employee.objects.get(id=u_employee_id)
            except:
                content["show_error"]="Employee does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            
            
            
            try:
                u_employee.manager  = Manager.objects.get(name=str(u_employee_manager))
            except:
                content["show_error"]="manager does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            try:
                u_employee.save()
            except:
                content["show_error"]="Employee's name is too long"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            
            return redirect("/Manager-Employee/")
        if "EmployeeAddStore" in request.POST:
            u_employee_store = request.POST["store_select"]
            u_employee_name = request.POST["employee_select"]
            try:
                u_employee = Employee.objects.get(name=u_employee_name)
                u_employee.e_store.add(Store.objects.get(name=str(u_employee_store)))
                
            except:
                content["show_error"]="store or manager does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            
            for s in u_employee.e_store.all():
                store_message+=s.name+" "
            
            content["show"]=store_message
            store_message=content["show"]
            u_employee.save()

        if "EmployeeRemoveStore" in request.POST:
            u_employee_store = request.POST["store_select"]
            u_employee_name = request.POST["employee_select"]
            try:
                u_employee = Employee.objects.get(name=u_employee_name)
                u_employee.e_store.remove(Store.objects.get(name=str(u_employee_store)))
                
            except:
                content["show_error"]="This store is not assigned to employee before"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            
           
            u_employee.save()
    return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"employees":employees, "show":store_message})


    

def managermenu(request):
    '''
    Functions for manage menu
    '''
    content={}
    content["show"]=""
    error_message=""
    menus = Menu.objects.all()
    
    # if request.method == 'POST' and request.FILES['myfile']:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'Manager-Menu.html', {
    #     'uploaded_file_url': uploaded_file_url})
   
    if request.method == "POST": 
        if "MenuAdd" in request.POST: 
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            

            id_for_dish = request.POST["id_for_dish"] 
            name_of_cuisine = request.POST["name_of_cuisine"] 
            try:
                price = int(request.POST['price'])
            except:
                content["show"]="price must be integer"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})
            category = request.POST['menu_select']
            description = request.POST['description']
            try:
                a_menu = Menu(picture=uploaded_file_url, id_for_dish=id_for_dish, name_of_cuisine=name_of_cuisine,price=price,classification=category,description=description)
                a_menu.save() 
            except:
                content["show"]="the input should comply with rules, check your input"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message}) 
            return redirect("/Manager-Menu/")
        if "MenuDelete" in request.POST: #checking if there is a request to delete a todo
            d_Menu_id = request.POST["MenuDelete"]
            try: 
                d_menu = Menu.objects.get(id=d_Menu_id) 
            except:
                content["show"]="menu does not exist"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})
            d_menu.delete()
            return redirect("/Manager-Menu/")
        if "MenuUpdate" in request.POST: #checking if there is a request to update
            try:
                myfile = request.FILES['myfileupdate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)

                u_Menu_id = request.POST["MenuUpdate"]
                u_Menu_id_dish = request.POST["input_menuid_for_dish"] 
                u_menu_name = request.POST["input_menuname_of_cuisine"]
                u_category = request.POST['menu_select']
                u_description = request.POST['input_menudescription']
            except:
                content["show"]="the input should comply with rules, check your input"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message}) 
            try:
                u_price = int(request.POST['input_menuprice'])
            except:
                content["show"]="price must be integer"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})
            try:
                u_menu = Menu.objects.get(id=u_Menu_id)
            except:
                content["show"]="menu does not exist"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})
            u_menu.id_for_dish = str(u_Menu_id_dish)
            u_menu.name_of_cuisine = str(u_menu_name)
            u_menu.classification = str(u_category)
            u_menu.description = str(u_description) 
            u_menu.price = str(u_price)  
            u_menu.picture = uploaded_file_url
            try:

                u_menu.save()
            except:
                content["show"]="the input should comply with rules, check your input"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message}) 
            return redirect("/Manager-Menu/")

    
    return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})

