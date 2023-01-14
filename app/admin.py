from django.contrib import admin
from .models import  Role, Employee


class roleAdmin(admin.ModelAdmin):
    list_display = ['name']


class employeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'jobRole']



admin.site.register(Role, roleAdmin)
admin.site.register(Employee, employeeAdmin)
