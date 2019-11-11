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
        self.driver.get("http://localhost:8100/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element_by_id("id_username").send_keys("nichole")
        pwd = self.driver.find_element_by_id("id_password").send_keys("123")
        loginbutton = self.driver.find_element_by_id("loginbtn").click()
        time.sleep(5)
        desk_no = self.driver.find_element_by_id("desk_no").send_keys("12")
        select_store = Select(self.driver.ﬁnd_element_by_id("store"))
        select_store.select_by_index(1)
        select_menu = Select(self.driver.ﬁnd_element_by_id("menu"))
        select_menu.select_by_index(1)
        amount = self.driver.find_element_by_id("amount").send_keys("2")
        loginbutton = self.driver.find_element_by_id("orderbtn").click()
        
        self.assertEqual(2, order.amount)
    # def test_order(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://localhost:8100/Order/")
    #     time.sleep(2)
    #     desk_no = self.driver.find_element_by_id("desk_no").send_keys("12")
    #     select_store = Select(self.driver.ﬁnd_element_by_id("store"))
    #     select_store.select_by_index(1)
    #     select_menu = Select(self.driver.ﬁnd_element_by_id("menu"))
    #     select_menu.select_by_index(1)
    #     amount = self.driver.find_element_by_id("amount").send_keys("2")
    #     loginbutton = self.driver.find_element_by_id("orderbtn").click()
    #     order = Order(desk_no="12")
    #     self.assertEqual(2, order.amount)

    # driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
    # driver.get('http://www.google.com/');
    # time.sleep(5) # Let the user actually see something!
    # search_box = driver.find_element_by_name('q')
    # search_box.send_keys('ChromeDriver')
    # search_box.submit()
    #  # Let the user actually see something!
    # driver.quit()
        
    

