from rest_framework import serializers
from .models import Employee, Role

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



class EmployeeSerializers(serializers.ModelSerializer):
    jobRole = RoleSerializers()

    # def create(self, validated_data):
    #     jobRole_data = validated_data.pop('jobRole')
    #     emp = Employee.objects.create(**validated_data)
    #     for jobRole_data in jobRole_data:
    #         Role.objects.create(jobRole=emp, **jobRole_data)
    #     return emp

    def to_internal_value(self, data):
         self.fields['jobRole'] = serializers.PrimaryKeyRelatedField(
             queryset=Role.objects.all())
         return super(EmployeeSerializers, self).to_internal_value(data)

    class Meta:
        model = Employee
        fields = ['id','name','email','phone','salary','bonus','jobRole','experienceInYears','hireDate']
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['jobRole'] = RoleSerializers(instance.jobRole).data
        return response
  
