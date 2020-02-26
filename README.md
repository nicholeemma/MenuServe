# Menuserve(Web application) 
is my independent course project for 17-437 / 17-637 at Carnegie Mellon University.  
## Attention
If you are having this course right now, please do not copy paste my code directly, or you will get failed.
<br>
The website link:
<BR>
  <b>http://menuservejiayueyaapp.azurewebsites.net/</b>
<br>
The final version of source code is in hw6_deployment branch. More readme and instructions can be found in hw6_deployment branch.
  
I created three groups in admin. 
<br>
One is customer, users who register will be defaultly categorized as customers. They have the permission to order. They can add orders and delete orders, and they can see the status of order in order page. They can only see the orders made by themselves. 
<br>
Second group is employee, they have the permissions to add/update/delete orders. 
<br>
Third group is manager, they have the permissions to add/update/delete orders, add/update/delete stores, employee and users.
I have created a manager account initially. If you want its credentials, please email me (jiayueya@andrew.cmu.edu).
 

## *Using the webiste*

1. You can first log in with the superuser account. You are entitled to add(update/delete) menu, add(update/delete) store, add(update/delete) user, add(update/delete) employee. You can first go to manageuser page, change some roles of users, and add them to manager, employee and assign store to them. (First create manager, then store, then employee)

2. In main page, you are supposed to see the pictures of menus, when the mouse moves over the pictures, the according prices will show up. The newly added pictures will be shown here as well. This is the page for visitors, who are not logged in yet.

3. Click "Registration" , you can register as a customer. When the register is done, your default role is customer.

4. When you have done the register, you will be automatically redirect to order.
<br>Choose the store and fill in desk_no,Click button "Order", a certain dish will be chosen. The chosen ones will be displayed at below. You can delete whichever you want. You can only see the orders made by yourself. This is the page for customers to order.
The above funtion is applied as Ajax. You can also go to "main" -->"order"-->"ajax order"(at the top of page). This page shows all the orders and reload every 5 seconds with ajax.
For checking Ajax function:
Add orders here: http://menuservejiayueyaapp.azurewebsites.net//Order/
Page will reload automatically: http://menuservejiayueyaapp.azurewebsites.net/Submitted-Order-ajax/   show the orders made last 5 seconds

5. If you are an employee or a manager, you will be redirect to the order page as well. There is button at the top right,"Main", you can click and enter into main page for management. If you are a customer, you cannot manage.

6. In manager-main page, there are menu, employee, manager and store buttons. Click each of them, will lead you to the according page to manage. The page is for managers.

7. For the menu page, you can enter in information and add a dish. You can upload a picture, the picture itself and url will show up. The added dish will be shown up at below, meanwhile you can edit the record of dishes and delete one by one. Attention: the drag down box will be filled in as well, otherwise the page will render mistake alert in red.

8. For the order page, employee or the manager will only be seen the orders made from the stores they are belong to. If the employ or the manager has not assigned a store, it will show mistakes.

8. How to create managers. 
<br>First, in manager-user page, change the role of a user into manager. At manager-manager page, you will be all users in the "manager" group, enter in the gender, and click "Add". 
Manager group and Manager class are different things.

9. How to create employees. 
<br>First, in manager-user page, change the role of a user into employee.
