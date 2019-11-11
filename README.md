
### Name: Jiayue Yang   Course: 17637 Web Application

## *Serverl things to notice*

## I would like to use 1 grace day for this homework5.
Reference:
https://docs.djangoproject.com/en/2.2/topics/testing/overview/#running-tests
1. enabledhostnames:
"http://hw5jiayueyamenuserve.azurewebsites.net"

'NAME': 'HW5MENUSERVE',
'HOST': 'jiayueyapostgreshw5.postgres.database.azure.com',
'USER': 'nichole@jiayueyapostgreshw5',
'PASSWORD':'Sasuke?1',


2. Because I mostly used "render", which cannot applied reverse url resoluton. I remained some orginal pratices in render. I have already applied reverse url resolution in "redirect" and the links in HTML files.

3. The most version control and git commits are in the master branch, hw5 directory. When I have done the most work, I started to transfer files to new branch(homework5)

4. There are "search" and filter functions at pages, they are not ready to work.

5. I created three groups in admin. One is customer, users who register will be defaultly categorized as customers. They have the permission to order. They can add orders and delete orders, and they can see the status of order in order page. They can only see the orders made by themselves. Second group is empployee, they have the permissions to add/update/delete orders. Third group is manager, they have the permissions to add/update/delete orders, add/update/delete stores, employee and users.
 
6. Updated the preload function of dropdown list based on suggestions from TA.



## *Using the webiste*

1. You can first log in with the superuser account (Name:cmuwebapps-manager, Password:WebAppsIsTheBestCourse). You are entitled to add(update/delete) menu, add(update/delete) store, add(update/delete) user, add(update/delete) employee. You can first go to manageuser page, change some roles of users, and add them to manager, employee and assign store to them. (First create manager, then store, then employee)

2. In main page, you are supposed to see the pictures of menus, when the mouse moves over the pictures, the according prices will show up. The newly added pictures will be shown here as well. This is the page for visitors, who are not logged in yet.

3. Click "Registration" , you can register as a customer. When the register is done, your default role is customer.

4. When you have done the register, you will be automatically redirect to order.
<br>Choose the store and fill in desk_no,Click button "Order", a certain dish will be chosen. The chosen ones will be displayed at below. You can delete whichever you want. You can only see the orders made by yourself. This is the page for customers to order.

5. If you are an employee or a manager, you will be redirect to the order page as well. There is button at the top right,"Main", you can click and enter into main page for management. If you are a customer, you cannot manage.

6. In manager-main page, there are menu, employee, manager and store buttons. Click each of them, will lead you to the according page to manage. The page is for managers.

7. For the menu page, you can enter in information and add a dish. You can upload a picture, the picture itself and url will show up. The added dish will be shown up at below, meanwhile you can edit the record of dishes and delete one by one. Attention: the drag down box will be filled in as well, otherwise the page will render mistake alert in red.

8. For the order page, employee or the manager will only be seen the orders made from the stores they are belong to. If the employ or the manager has not assigned a store, it will show mistakes.

8. How to create managers. 
<br>First, in manager-user page, change the role of a user into manager. At manager-manager page, you will be all users in the "manager" group, enter in the gender, and click "Add". 
Manager group and Manager class are different things.

9. How to create employees. 
<br>First, in manager-user page, change the role of a user into employee.
At manager-employee page, you will be all users in the "employee" group you can add a new employee or add an existing employee to another existing store. The details will be shown at below.

10. The order of adding records is firstly adding a manager, then store, then adding employee. The creation of orders can be made after menu records exist.

11. The relationship between managers and stores is one manager can many stores, but one store can only have one manager. The employee can have many stores, but one manager. One record of menu can have many orders.

12. Clicking "log out" button can log out.