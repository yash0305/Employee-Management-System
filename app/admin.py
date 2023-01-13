from django.contrib import admin
from .models import Department, Role, Employee

class departmentAdmin(admin.ModelAdmin):
    list_display = ['name']


class roleAdmin(admin.ModelAdmin):
    list_display = ['name']


class employeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'department', 'jobRole']



admin.site.register(Department, departmentAdmin)
admin.site.register(Role, roleAdmin)
admin.site.register(Employee, employeeAdmin)
