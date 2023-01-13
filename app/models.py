from django.db import models
from django.core.exceptions import ValidationError
import datetime
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?91?\d{10}$', message="Mobile number should contain 10 digits")
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    jobRole = models.ForeignKey(Role, on_delete=models.CASCADE)
    experienceInYears = models.IntegerField(default=0)
    hireDate = models.DateField()
    

    # def checkMobileNumberLength(self):
    #     a = len(str(self.phone))
    #     if a == 10:
    #         return False
    #     else:
    #         return True

    def isHiredateNotPast(self):
        todayDate = datetime.date.today()
        if self.hireDate > todayDate:
            return True
        else:
            return False

    def clean(self):
        # if self.checkMobileNumberLength():
        #     raise ValidationError('Mobile number should contain 10 digits')
        if self.isHiredateNotPast():
            raise ValidationError('Only current date and past dates are allowed')
