# MenuServe(Web application) 
is my independent course project for 17-437 / 17-637 at Carnegie Mellon University. 
<br>
It is basically a restaurant information management system for customers to order and for managers to manage employees.

<br>
## Link & Code

<BR>
  <b>http://menuservejiayueyaapp.azurewebsites.net/</b>
<br>
The final version of source code is in hw6_deployment branch. More readme and instructions can be found in hw6_deployment branch.
 <br>

## Technology

- Python (Django MVC framework)
- Postgres as Database
- HTML, CSS(Bootstrap), JavaScript, JQuery(Ajax)
- CI/CD tool, Azure deployment
- Git

## Main Functions
  - Registration and Login

  - Authentication (Accessibility of functions is role-based)

  - Menu management (Update, delete, add) (Support image uploading)

  - Employee management (Manager, employee, store information management)

     (The relationship between employees and stores is many to many)

  - Order Management

  - View orders (Automatic refreshing)

  - Input checking (illegal input will render error message)

  <br>
I created three groups in admin. 
<br>
One is customer, users who register will be default categorized as customers. They have the permission to order. They can add orders and delete orders, and they can see the status of order in order page. They can only see the orders made by themselves. 
<br>
Second group is employee, they have the permissions to add/update/delete orders. 
<br>
Third group is manager, they have the permissions to add/update/delete orders, add/update/delete stores, employee and users.


## Instructions

1. In main page, you are supposed to see the pictures of menus, when the mouse moves over the pictures, the according prices will show up. The newly added pictures will be shown here as well. This is the page for visitors, who are not logged in yet.

2. You can first log in with the superuser account. 

   (I have pre-created a manager account for testing. The username is *superuser*, password is *superuser*.) 

   You are entitled to add(update/delete) menu, add(update/delete) store, add(update/delete) user, add(update/delete) employee.

   When you are logged in as a manager(superuser), you can see a "main" button at the right top. (Customers won't be able to see this button) You can go to [All-User](http://menuservejiayueyaapp.azurewebsites.net/Manager-User/), change some roles of users, and add them to manager, employee and assign store to them. (First create manager, then store, then employee)

3. How to create managers.  

   First, in [Manager-user](http://menuservejiayueyaapp.azurewebsites.net/Manager-User/), change the role of a user into manager class. At [Manager-manager](http://menuservejiayueyaapp.azurewebsites.net/Manager-Manager/ )

    you will see all users in the "manager" group, enter in the gender, and click "Add", after that a manager is created successfully.  Manager group and Manager class are different things.

4. In manager-main page, there are menu, employee, manager and store buttons. Click each of them, will lead you to the according page to manage. The page is for managers.

5. How to create store

   In [Manager-store](http://menuservejiayueyaapp.azurewebsites.net/Manager-Store/ ), fill in name, location and assign a manager to this store.

   A store can only have one manager, one manager can manage multiple stores.

6. How to create employees. 

    In manager-user page, change the role of a user into employee. Then go to [manager-employee](http://menuservejiayueyaapp.azurewebsites.net/Manager-Employee/ ),you will see names from employee group, you have to assign a manager and a store to this employee, after that an employee is successfully added to the restaurant. You cannot add an existing employee second time or error message will show up. After adding, the information will show up below, you can change manager or delete this employee from restaurant. In addition, an employee can serve multiple stores, so you can add a store or remove a store to an assigned employee.

7. Click "Registration" , you can register as a customer. When the register is done, your default role is customer. You can view the menu and order.

8. When you have done the register, you will be automatically redirect to order.
  Choose the store and fill in desk_no, order whatever dish you want. The chosen ones will be displayed at below using Ajax without refreshing. You can delete whichever you want. You can only see the orders made by yourself. This is the page for customers to order.

9. If you are an employee or a manager. You can see all the submitted orders. You can also go to "main" -->"order"-->"ajax order"(at the top of page). This page shows all the orders and reload every 5 seconds with ajax.
  For checking Ajax function:
  Add orders here: http://menuservejiayueyaapp.azurewebsites.net/Order/
  Page will reload automatically: http://menuservejiayueyaapp.azurewebsites.net/Submitted-Order-ajax/   show the orders made last 5 seconds

10. For the menu page, you can enter in information and add a dish. You can upload a picture, the picture itself and the url will show up. The added dish will be shown up at below, meanwhile you can edit the record of dishes and delete one by one. Attention: the drag down box will be filled in as well, otherwise the page will render mistake alert in red.

11. For the order page, employee or the manager will only be seen the orders made from the stores they are belong to. If the employ or the manager has not assigned a store, it will show mistakes.

    


## Attention!!!
If you are having this course right now, please do not copy paste my code directly, or you will get failed.