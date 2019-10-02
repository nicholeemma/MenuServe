
### Name: Jiayue Yang   Course: 17637 Web Application

## *Serverl things to notice*
1. enabledhostnames:
"menuservejiayueya.azurewebsites.net"

 'NAME': os.environ['DBNAME'],
 menuserve
    'HOST': os.environ['DBHOST'],
     jiayueyapostgresql.postgres.database.azure.com 
    'USER': os.environ['DBUSER'],
    jiayueya@jiayueyapostgresql
    'PASSWORD':os.environ['DBPASS'],
    Sasuke?1

2. Because I mostly used "render", which cannot applied reverse url resoluton. I remained some orginal pratices in render. I have already applied reverse url resolution in "redirect" and the links in HTML files.

3. Before professor's announcement, I have already copied branch files to master. I know it is a unnecessay step, please grade base on the hw4_deployment branch.

4. As the postgres database is extremely strict with data type. There some small length of variables. If your input exceeds the length, an error will jump out.
See more details in model.py. 
id_for_dish and desk_no 's length are only 4. Please pay attention to this when entering value.

5. More futher validation will be done in next assignment I think. The error message might be simple and not easy to figure out what was the problem.

6. Last assignment, Enes suggested me to do the preload dropdown list. I have not figured out how to do that, I think it will use jQuery, so I will leave it to next assignment to implement.

7. As it is extremely inconvenient to check results after deploying to Azure, the commit messages might be repetive. Becase I was keeping check the result after I made some changes to the code.

## *Using the webiste*

1. In main page, you are supposed to see the pictures of menus, when the mouse moves over the pictures, the according prices will show up. The newly added pictures will be shown here as well. This is the page for visitors, who are not logged in yet.

2. Click "Registration/ Log in" to jump to the order page. (In the future, some validation will be implemented)
All available menu will be displayed.
Choose the store and fill in desk_no,**(please note the length of desk_no is only 4, if the input exceeds the length, an error will jump out )and amount(integer)**. Click button "Order", a certain dish will be chosen. The chosen ones will be displayed at below. You can delete whichever you want. This is the page for customers to order.

3. Click the bottom "Order" button to jump to the submitted order page. This is the page for employees or managers to view the orders. They can edit or delete orders. The upper part of each row is for employee to edit, the down part of each row shows the current details of orders. [The entrance of adding orders is in order page]

4. At the top right corner, there is button named "main". It will lead you to manager-main page. For now, it is the only way to go to manager-main page. 

5. In manager-main page, there are menu, employee, manager and store buttons. Click each of them, will lead you to the according page to manage. The page is for managers.

6. For the menu page, you can enter in information and add a dish. You can upload a picture, the picture itself and url will show up. The added dish will be shown up at below, meanwhile you can edit the record of dishes and delete one by one. Attention: the drag down box will be filled in as well, otherwise the page will render mistake alert in red.

7. For the employee, manager, store, they are similar.

8. For the employee page, you can add a new employee or add an existing employee to another existing store. The details will be shown at below.

9. The order of adding records is firstly adding a manager, then store, since there is an attribute in store which is manager, then adding employee. The creation of orders can be made after menu records exist.

10. The relationship between managers and stores is one manager can many stores, but one store can only have one manager. The employee can have many stores, but one manager. One record of menu can have many orders.

11. Clicking "log out" button can go back to manager-main page.