from django.test import TestCase

# Create your tests here.
from .models import Menu, Store, Employee, Manager, Order
from django.contrib.auth.models import User

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
        
    

