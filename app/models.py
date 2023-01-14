from django.db import models
from django.core.exceptions import ValidationError
import datetime
from django.core.validators import RegexValidator



class Role(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+91+\d{10}$', message="Mobile number should contain 10 digits")
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    jobRole = models.ForeignKey(Role, on_delete=models.CASCADE)
    experienceInYears = models.IntegerField(default=0)
    hireDate = models.DateField()
    

 

    def isHiredateNotPast(self):
        todayDate = datetime.date.today()
        if self.hireDate > todayDate:
            return True
        else:
            return False

    def clean(self):
        if self.isHiredateNotPast():
            raise ValidationError('Only current date and past dates are allowed')
