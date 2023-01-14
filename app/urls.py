from django.urls import path
from .views import employeeCreate, employeeList, employeeDelete, employeeDetail, employeeUpdate 
  
urlpatterns = [
    # path('hello/', HelloView.as_view(), name ='hello'),
    path('employee-create/', employeeCreate, name ='employee-create'),
    path('employee-list/', employeeList, name ='employee-list'),
    path('employee-delete/<str:pk>/', employeeDelete, name ='employee-delete'),
    path('employee-update/<str:pk>/', employeeUpdate, name ='employee-update'),
    path('employee-detail/<str:pk>/', employeeDetail, name ='employee-detail'),


]
