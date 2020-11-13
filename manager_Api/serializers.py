from rest_framework import serializers
from employees.models import Employee
from django.conf import settings


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'email', 'first_name', 'last_name', 'address', 'dob', 'company', 'mobile', 'city')

# class UserRegisterSerializer(serializers.ModelSerializer):

#     email = serializers.EmailField(required=True)
#     first_name = serializers.CharField(required=True)
#     password = serializers.CharField(min_length=8, write_only=True)

#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('email', 'first_name', 'last_name', 'address', 'dob', 'company')
#         extra_kwargs = {'password': {'write_only': True}}