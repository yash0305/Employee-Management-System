
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Role
from rest_framework.decorators import permission_classes, api_view
from .serializers import EmployeeSerializers, RoleSerializers
from datetime import datetime
from datetime import date

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employeeList(request):
    emp = Employee.objects.all()
    s = EmployeeSerializers(emp, many=True)
    return Response(s.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employeeDetail(request,pk):
    emp = Employee.objects.get(id = pk)
    s = EmployeeSerializers(emp, many=False)
    return Response(s.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def employeeCreate(request):

    data = request.data
    hireDate = data["hireDate"]
    hireDate = datetime.strptime(hireDate, "%Y-%m-%d").date()
    today = date.today()

    if not(hireDate > today):
        s = EmployeeSerializers(data=request.data)
        print(f"hire condition {s}")
    else: 
        return Response("Only current date and past dates are allowed")
    if s.is_valid():
        s.save()
        # print(f"valid condition {s}")
    return Response(s.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def employeeUpdate(request,pk):
    emp = Employee.objects.get(id = pk)
    s = EmployeeSerializers(instance=emp,data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def employeeDelete(request,pk):
    emp = Employee.objects.get(id = pk)
    emp.delete()
    return Response("Employee succesfully deleted")



