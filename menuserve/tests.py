from django.test import TestCase, LiveServerTestCase
# Create your tests here.
from .models import Menu, Store, Employee, Manager, Order
from django.contrib.auth.models import User
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class MenuserveTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        Menu.objects.create(name_of_cuisine="hellodish", id_for_dish="12", price=9, classification="seafood", description="des")
        
        # Employee.objects.create(name="cat", sound="meow")
        m = Manager.objects.create(manageruser=self.user, gender="male")
        m.save()
        # manager_ = Manager(manageruser=self.user)
        store = Store.objects.create(location="Pitts", store_manager=m, name="happy" )
        store.save()
        
       
    def test_user(self):
        """Animals that can speak are correctly identified"""
        
        self.assertEqual(self.user.username, 'jacob')
    def test_menu(self):
        t_menu = Menu(name_of_cuisine="hellodish")
        self.assertEqual("hellodish", t_menu.name_of_cuisine)
    def test_manager(self):
        t_manager = Manager(manageruser=self.user)
        self.assertEqual(self.user, t_manager.manageruser)
    def test_store(self):
        t_store = Store(name="happy")
        self.assertEqual("happy", t_store.name)
    def test_order(self):
        manager_ = Manager(manageruser=self.user)
        store_ = Store(location="Pitts1", store_manager=manager_, name="happy1")
        store_.save()
        t_order = Order.objects.create(desk_no="12", name_of_cuisine="burgerplus",status="pending",amount=6,price=8,store=store_,order_user=self.user)
        t_order.save()
       
        self.assertEqual(8, t_order.price)
    def test_employee(self):
        manager_ = Manager(manageruser=self.user)
        t_employee = Employee(employeeuser = self.user,manager=manager_)
        # SAVE IS IMPORTANT HERE
        t_employee.save()
        store_ = Store(location="Pitts11", store_manager=manager_, name="happy1")
        store_.save()
        t_employee.e_store.add(store_)



class FrontEndTest(LiveServerTestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='jaco', email='jacob@…', password='top_secret')
    def test_login(self):

        self.driver = webdriver.Chrome()
        # self.live_server_url+
        self.driver.get("http://localhost:8100/accounts/login/")
        # Test case for log in
        time.sleep(2)
        username = self.driver.find_element_by_id("id_username").send_keys("cmuwebapps-manager")
        pwd = self.driver.find_element_by_id("id_password").send_keys("WebAppsIsTheBestCourse")
        loginbutton = self.driver.find_element_by_id("loginbtn").click()
        # Test case for ordering 
        time.sleep(5)
        desk_no = self.driver.find_element_by_id("desk_no").send_keys("12")
        select_store = Select(self.driver.ﬁnd_element_by_id("store"))
        select_store.select_by_index(1)
        select_menu = Select(self.driver.ﬁnd_element_by_id("menu"))
        select_menu.select_by_index(1)
        amount = self.driver.find_element_by_id("amount").send_keys("2")
        orderbutton = self.driver.find_element_by_id("orderbtn").click()
        time.sleep(2)
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        # Test case for entering the managermain page
        orderbutton = self.driver.find_element_by_id("management-main-menu").click()
        # Test case for updating a menu
        update = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[2]/td[2]/input").send_keys("0")
        time.sleep(1)
        updatebtn = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[2]/td[8]/button").click()
        time.sleep(2)
        # go back to manager main page
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        time.sleep(2)
        # Test case for viewing order page and update an order
        orderbutton = self.driver.find_element_by_id("management-main-order").click()
        time.sleep(2)
        updatedeskno = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@id='order_']/tbody/tr[1]/td[3]/input").send_keys("8")
        time.sleep(2)
        # DO NOT PUT BUTTON ID HERE, BECAUSE THE ID WILL CHANGE, JUST LOCATE TO THE FIRST BUTTON
        updatebtn = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@id='order_']/tbody/tr[1]/td[9]/button").click()
        time.sleep(2)
        # go back to manager main page
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        time.sleep(2)
        # Test case: change role for user
        userbutton = self.driver.find_element_by_id("management-main-user").click()
        time.sleep(1)
        selectrole = Select(self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[1]/td[6]/select[@id='user-role']"))
        selectrole.select_by_index(1)
        time.sleep(1)
        rolebtn = self.driver.find_element_by_xpath("//body/div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[1]/td[7]/button").click()
        time.sleep(1)
        # go back to manager main page
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        # Test case: update information for a manager
        managerbutton = self.driver.find_element_by_id("management-main-manager").click()
        time.sleep(1)
        genderupd = self.driver.find_element_by_xpath("//body/div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr/td[3]/input").send_keys("emale")
        time.sleep(1)
        upbtn = self.driver.find_element_by_xpath("//body/div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr/td[4]/button").click()
        time.sleep(1)
        # go back to manager main page
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        # Test case: create a new store
        storebutton = self.driver.find_element_by_id("management-main-store").click()
        time.sleep(1)
        namestore = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[1]/td[2]/input[@id='status']").send_keys("Store-B")
        time.sleep(1)
        locstore = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[1]/td[3]/input[@id='status']").send_keys("pit")
        time.sleep(1)
        selectm = Select(self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[1]/td[4]/select[@id='manager']"))
        selectm.select_by_index(1)
        time.sleep(1)
        createstore = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[1]/td[5]/button[@class='waves-effect waves-light btn']").click()
        time.sleep(1)
        # go back to manager main page
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        # Test case: Add an employee to a store
        ebutton = self.driver.find_element_by_id("management-main-employee").click()
        eselect = Select(self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[2]/td[1]/select[@id='manager']"))
        eselect.select_by_index(1)
        sselect = Select(self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[2]/td[2]/select[@id='store']"))
        sselect.select_by_index(1)
        btn = self.driver.find_element_by_xpath("//div[@id='maincontainer']/div[@class='general-container']/div[@class='record-table']/table[@class='striped']/tbody/tr[2]/td[3]/button[@class='waves-effect waves-light btn']").click
        # go back to manager main page
        mainbutton = self.driver.find_element_by_id("mainbtn").click()
        # log out
        logoutbutton = self.driver.find_element_by_id("logout").click()
    


 
    

