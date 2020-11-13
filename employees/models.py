from django.db import models
from django.conf import settings
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Employee(models.Model):
    emp_id = models.CharField(max_length=70, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    company = models.CharField(max_length=50)
    mobile = models.CharField(max_length=70, default="")
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
