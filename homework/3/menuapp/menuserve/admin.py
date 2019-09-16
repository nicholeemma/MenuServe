from django.contrib import admin

# Register your models here.
from . import models
class StoreAdmin(admin.ModelAdmin):
    list_display = ("location",  "name")
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",)
# admin.site.register(models.TodoList, TodoListAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name_of_cuisine",  "id_for_dish","price","classification","description")

class ManagerAdmin(admin.ModelAdmin):
    list_display = ("name",  "m_store")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("desk_no",  "name_of_cuisine","status","time","amount","store")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name",  "e_store","manager")

admin.site.register(models.Store, StoreAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Manager, ManagerAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Employee, EmployeeAdmin)