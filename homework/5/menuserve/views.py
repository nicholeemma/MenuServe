from django.shortcuts import render,redirect, get_object_or_404
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Menu, Store, Employee, Manager, Order,Document
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
#Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404
# Used to generate a one-time-use token to verify a user's email address
from django.contrib.auth.tokens import default_token_generator
from django.db import transaction
from .forms import StoreForm,StoreUpdateForm,ManagerForm,ManagerUpdateForm,EmployeeForm,EmployeeUpdateForm,MenuForm,MenuUpdateForm, OrderForm,OrderUpdateForm

# Used to send mail from within Django
from django.core.mail import send_mail
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
                content["show"]="something wrong with input"
                error_message = content["show"]
                return redirect(reverse("index"))
                #return render(request,"Menu.html",{"menus":menus,"show":error_message})
        if "select" in request.POST:
            menus = ""
            try:
                # getlist method is important to remember
                checkedlist = request.POST.getlist('checkedbox')
                #checkedlist = request.POST["checkedbox"] 
                for checked_classification in checkedlist:
                    
                    menus = Menu.objects.filter(classification=checked_classification)
                   
            except:
                content["show"]="something wrong with input"
                error_message = content["show"]
                return redirect(reverse("index"))
                #return render(request,"Menu.html",{"menus":menus,"show":error_message})
    
    
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

            form = OrderForm(request.POST) 
            if form.is_valid():
            
                amount = form.cleaned_data["amount"]
                desk_ = form.cleaned_data["desk_no"]
            else:
                content["show"]=form.errors
                error_message = content["show"]
                return render(request,"Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            
            store_ = request.POST["store_select"]
            
            name_of_cuisine = Menu.objects.get(id = menu_id).name_of_cuisine
            price = Menu.objects.get(id = menu_id).price * amount
            try:
                store = Store.objects.get(id=str(store_))
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
            return redirect(reverse("Order"))    
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
            form = OrderUpdateForm(request.POST) 
            if form.is_valid():
                u_input_desk_no = form.cleaned_data["input_desk_no"]
                u_input_amount = form.cleaned_data["input_amount"]
            else:
                content["show"] = form.errors
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message})
               
            u_cuisine_select = request.POST["cuisine_select"] 
                        
            u_input_status = request.POST["input_status"]
            #u_input_time = request.POST["input_time"]
            
            u_input_store = request.POST["store_select"]
            try:
                u_order = Order.objects.get(id = u_id)
            except:
                content["show"]="order does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message})
              
            u_order.desk_no = str(u_input_desk_no)
            u_order.name_of_cuisine = str(u_cuisine_select)
            u_order.status = u_input_status
           
            u_order.amount = u_input_amount
            try:
                u_order.price = int(int(Menu.objects.get(name_of_cuisine = u_cuisine_select).price)*int(u_input_amount))
            except:
                content["show"]="menu does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message})               
            #u_order.time = u_input_time
            try:
                u_order.store = Store.objects.get(id = str(u_input_store ))
            except:
                content["show"]="Store does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 
            


            u_order.save()
            return redirect(reverse("manageorder"))

        if "DeleteUpdate" in request.POST: #checking if there is a request to delete a todo
            d_order = request.POST["DeleteUpdate"] #checked todos to be deleted
            try:
                delete_order = Order.objects.get(id=int(d_order)) #getting todo id
            except:
                content["show"]="Order does not exist"
                error_message = content["show"]
                return render(request,"Submitted-Order.html",{"orders":orders,"stores":stores,"menus":menus,"show":error_message}) 

            delete_order.delete() #deleting todo
            return redirect(reverse("manageorder"))
            #return redirect("/Submitted-Order/")

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
            form = StoreForm(request.POST) 
            if form.is_valid():
                location = form.cleaned_data["location"] 
                name = form.cleaned_data["name"] 
                manager_name = form.cleaned_data["manager_select"]
                manager = Manager.objects.get(name=str(manager_name))
                a_store = Store(name=name, location=location,store_manager=manager)
                a_store.save() 
            else:
                #content["show"]=form.errors.get("name",None)
                content["show"]=str(form.errors)
                #content["show"]="Not correct"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            return redirect(reverse("managerstore"))
            #return redirect("/Manager-Store/")
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
            return redirect(reverse("managerstore"))
            #return redirect("/Manager-Store/")
        if "StoreUpdate" in request.POST: 
            form = StoreUpdateForm(request.POST)
            if form.is_valid():
                u_store_id = form.cleaned_data["StoreUpdate"]
                u_store_location = form.cleaned_data["input_storelocation"]            
                u_store_name = form.cleaned_data["input_storename"]
                u_store_manager = form.cleaned_data["manager_select"]
                u_store = Store.objects.get(id=u_store_id)
                u_store.location = str(u_store_location)
                u_store.name = str(u_store_name)
            else:
                content["show"]=str(form.errors)
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 
            try:
                u_store.store_manager  = Manager.objects.get(name=str(u_store_manager))
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Store.html",{"stores":stores,"managers":managers,"show":error_message}) 

            #getting todo id
            u_store.save()
            return redirect(reverse("managerstore"))
            #return redirect("/Manager-Store/")


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
            form = ManagerForm(request.POST) 
            if form.is_valid():
                gender = form.cleaned_data["gender"] 
                name = form.cleaned_data["name"] 
                a_manager = Manager(name=name, gender=gender)
                a_manager.save() 
            else:
                content["show"]=str(form.errors)
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
            return redirect(reverse("managermanager"))
            #return redirect("/Manager-Manager/")
        if "ManagerDelete" in request.POST: #checking if there is a request to delete a todo
            d_manager_id = request.POST["ManagerDelete"] #checked todos to be deleted
            try:
                d_manager = Manager.objects.get(id=d_manager_id) #getting todo id
            except:
                content["show"]="Manager does not exist"
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
            d_manager.delete()
            return redirect(reverse("managermanager"))
            #return redirect("/Manager-Manager/")
        if "ManagerUpdate" in request.POST:
            form = ManagerUpdateForm(request.POST) 
            if form.is_valid():
                u_manager_id = request.POST["ManagerUpdate"]
                u_manager_gender = form.cleaned_data["input_managergender"] #checked todos to be deleted          
                u_manager_name = form.cleaned_data["input_managername"]           
                u_manager = Manager.objects.get(id=u_manager_id)
            else:
                content["show"]=str(form.errors)
                error_message = content["show"]
                return render(request,"Manager-Manager.html",{"managers":managers,"show":error_message}) 
            u_manager.gender = str(u_manager_gender)
            u_manager.name = str(u_manager_name)  
            u_manager.save()
            return redirect(reverse("managermanager"))
            #return redirect("/Manager-Manager/")    
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
            form = EmployeeForm(request.POST) 
            if form.is_valid():
                name = form.cleaned_data["name"] 
                
            else:
                content["show_error"] = str(form.errors)
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees}) 
            try:
                manager_name = request.POST["manager_select"]
                manager = Manager.objects.get(id=str(manager_name))
            except:                
                content["show_error"]="Manager does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees}) 
            
            store_name = request.POST["store_select"]
            try:
                store = Store.objects.get(id=str(store_name))
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
            return redirect(reverse("manageremployee"))
            #return redirect("/Manager-Employee/")
        if "EmployeeUpdate" in request.POST: 
            u_employee_id = request.POST["EmployeeUpdate"]
            form = EmployeeUpdateForm(request.POST) 
            if form.is_valid():
                u_employee_name = form.cleaned_data["input_employeename"]
                u_employee_manager = request.POST["manager_select"]
            else:
                
                content["show_error"]=form.errors
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
            
            
            try:
                u_employee = Employee.objects.get(id=u_employee_id)
            except:
                content["show_error"]="Employee does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id

            try:
                u_employee.manager  = Manager.objects.get(id=str(u_employee_manager))
            except:
                content["show_error"]="manager does not exist"
                error_message = content["show_error"]
                return render(request,"Manager-Employee.html",{"stores":stores,"managers":managers,"show_error":error_message,"employees":employees})  #getting todo id
        
            u_employee.save()
            return redirect(reverse("manageremployee"))
            #return redirect("/Manager-Employee/")

        if "EmployeeAddStore" in request.POST:
            u_employee_store = request.POST["store_select"]
            u_employee_name = request.POST["employee_select"]
            try:
                u_employee = Employee.objects.get(id=u_employee_name)
                u_employee.e_store.add(Store.objects.get(id=str(u_employee_store)))
                
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
                u_employee = Employee.objects.get(id=u_employee_name)
                u_employee.e_store.remove(Store.objects.get(id=str(u_employee_store)))
                
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
            try:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
            except:
                content["show"]="Please upload correct pictures"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message}) 
            form = MenuForm(request.POST) 
            if form.is_valid():
                id_for_dish = form.cleaned_data["id_for_dish"] 
                name_of_cuisine = form.cleaned_data["name_of_cuisine"]            
                price = form.cleaned_data['price']
                category = form.cleaned_data['menu_select']
                description = form.cleaned_data['description']

                # myfile = request.FILES['myfile']
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
            else:
                content["show"]=form.errors
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})
            
            a_menu = Menu(picture=uploaded_file_url, id_for_dish=id_for_dish, name_of_cuisine=name_of_cuisine,price=price,classification=category,description=description)
            a_menu.save() 
            
            return redirect(reverse("managermenu"))
            #return redirect("/Manager-Menu/")
        if "MenuDelete" in request.POST: #checking if there is a request to delete a todo
            d_Menu_id = request.POST["MenuDelete"]
            try: 
                d_menu = Menu.objects.get(id=d_Menu_id) 
            except:
                content["show"]="menu does not exist"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})
            d_menu.delete()
            return redirect(reverse("managermenu"))
            #return redirect("/Manager-Menu/")
        if "MenuUpdate" in request.POST: #checking if there is a request to update
            try:
                myfile = request.FILES['myfileupdate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
            except:
                content["show"]="Choose a correct file please"
                error_message = content["show"]
                return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message}) 
            form = MenuUpdateForm(request.POST) 
            u_Menu_id = request.POST["MenuUpdate"]
            if form.is_valid():
                u_Menu_id = form.cleaned_data["MenuUpdate"]
                u_Menu_id_dish = form.cleaned_data["input_menuid_for_dish"] 
                u_menu_name = form.cleaned_data["input_menuname_of_cuisine"]
                u_category = form.cleaned_data['menu_select']
                u_description = form.cleaned_data['input_menudescription']
                u_price = form.cleaned_data['input_menuprice']
            else:
                content["show"]=form.errors
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
            u_menu.save()
            return redirect(reverse("managermenu"))
            #return redirect("/Manager-Menu/")

    
    return render(request,"Manager-Menu.html",{"menus":menus,"show":error_message})

@transaction.atomic
def registration(request):
    context = {}

    if request.method == 'GET':
        return render(request, '/registration/registration.html', context)

    errors = []
    context['errors'] = errors

	# Checks the validity of the form data
    if not 'username' in request.POST or not request.POST['username']:
        errors.append('Username is required.')
    else:
        # Save the username in the request context to re-fill the username
        # field in case the form has errrors
        context['username'] = request.POST['username']


    if len(User.objects.filter(username = request.POST['username'])) > 0:
        errors.append('Username is already taken.')

    if errors:
        return render(request, 'registration/registration.html', context)

    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'], \
                                        password=request.POST['password'], email=request.POST['email'])
    new_user.is_active = False
    new_user.save()

     # Generate a one-time use token and an email message body
    token = default_token_generator.make_token(new_user)

    email_body = """
Welcome to the Simple Address Book.  Please click the link below to
verify your email address and complete the registration of your account:
  http://%s%s""" % (request.get_host(),
       reverse('confirm', args=(new_user.username, token)))

    send_mail(subject="Verify your email address",
              message= email_body,
              from_email="jiayueya@andrew.cmu.edu",
              recipient_list=[new_user.email])

    context['email'] = request.POST['email']

    # Logs in the new user and redirects to his/her todo list
   # new_user = authenticate(username=request.POST['username'], \
    #                        password=request.POST['password'])
   # login(request, new_user)
    return render(request, 'registration/needs_confirmation.html', context)

@transaction.atomic
def confirm_registration(request, username, token):
    user = get_object_or_404(User, username=username)

    # Send 404 error if token is invalid
    if not default_token_generator.check_token(user, token):
        raise Http404

    # Otherwise token was valid, activate the user.
    user.is_active = True
    user.save()
    return render(request, 'registration/confirmed.html', {})