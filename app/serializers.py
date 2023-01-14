from rest_framework import serializers
from .models import Employee, Role

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','email','phone','salary','bonus','jobRole','experienceInYears','hireDate']
    
   