from django.shortcuts import get_object_or_404
from rest_framework import generics
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

class EmployeeList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployee(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditEmployee(generics.UpdateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class DeleteEmployee(generics.RetrieveDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
