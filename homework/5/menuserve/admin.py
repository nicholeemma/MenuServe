from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from . import models
class StoreAdmin(admin.ModelAdmin):
    list_display = ("location",  "name","store_manager")
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",)
# admin.site.register(models.TodoList, TodoListAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name_of_cuisine",  "id_for_dish","price","classification","description")

class ManagerAdmin(admin.ModelAdmin):
    list_display = ("manageruser_","gender")
    def manageruser_(self, obj):
        return str(obj.user.username)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("desk_no",  "name_of_cuisine","status","time","amount","store")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employeeuser_",  "e_store_","manager_")
    def e_store_(self, obj):
        return "\n".join([s.name for s in obj.e_store.all()])
    def manager_(self, obj):
        return str(obj.manager.name)
    def employeeuser_(self, obj):
        return str(obj.user.username)
admin.site.register(models.Store, StoreAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Manager, ManagerAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Employee, EmployeeAdmin)