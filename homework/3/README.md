### Name: Jiayue Yang   Course: 17637 Web Application

1. In main page(localhost:), you are supposed to see the pictures of menus, when the mouse moves over the pictures, the according prices will show up. This is the page for visitors, who are not logged in yet.

2. Click "Registration/ Log in" to jump to the order page. (In the future, some validation will be implemented)
All available menu will be displayed.
Choose the store and fill in desk_no, and amount. Click button "Order", a certain dish will be chosen. The chosen ones will be displayed at below. You can delete whichever you want. This is the page for customers to order.

3. Click the bottom "Order" button to jump to the submitted order page. This is the page for employees or managers to view the orders. They can edit or delete orders. The upper part of each row is for employee to edit, the down part of each row shows the current details of orders.

4. At the top right corner, there is button named "main". It will lead you to management page. 

5. In manager-main page, there are menu, employee, manager and store buttons. Click each of them, will lead you to the according page to manage. The page is for managers.

6. For the menu page, you can enter in information and add a dish. The added dish will be shown up at below, meanwhile you can edit the record of dishes and delete one by one. Attention: the drag down box will be filled in as well, otherwise the page will render mistake alert in red.

7. For the employee, manager, store, they are similar.

8. For the employee page, you can add a new employee or add an existing employee to another existing store. The details will be shown at below.

9. Remember, the order of adding records is firstly adding a manager, then store, since there is an attribute in store which is manager, then adding employee. The creation of orders can be made after menu records exist.

10. The relationship between managers and stores is one manager can many stores, but one store can only have one manager. The employee can have many stores, but one manager. One record of menu can have many orders.