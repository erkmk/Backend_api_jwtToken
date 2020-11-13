from django.urls import path
from .views import EmployeeList, CreateEmployee, EditEmployee, DeleteEmployee


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'manager_Api'

urlpatterns = [
    path('', EmployeeList.as_view(), name='listcreate'),

    # Post Admin URLs
    path('admin/create/', CreateEmployee.as_view(), name='createemployee'),
    path('admin/edit/<int:pk>/', EditEmployee.as_view(), name='editemployee'),
    path('admin/delete/<int:pk>/', DeleteEmployee.as_view(), name='deleteemployee'),
]
