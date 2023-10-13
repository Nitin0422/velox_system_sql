from django.db import models
import os
from django.core.exceptions import ValidationError

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=200)
    no_of_employees = models.IntegerField()

    def __str__(self):
        return self.department_name

class DepartmentGroup(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(DepartmentGroup, on_delete=models.DO_NOTHING)
    employee_full_name = models.CharField(max_length=200)
    employee_contact_number = models.CharField(max_length=200)
    employee_address = models.CharField(max_length=200)
    employee_PAN = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.employee_full_name

class Customer(models.Model):
    customer_full_name = models.CharField(max_length=200)
    customer_phone_number = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_full_name

class TaskCategory(models.Model):
    task_category_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete= models.DO_NOTHING, null=True)

    def __str__(self):
        return self.task_category_name

class TaskCode(models.Model):
    task_category = models.ForeignKey(TaskCategory, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    task_date = models.DateField()

    def __str__(self):
        return str(self.id)

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # extracts the extension of file 
    valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class Invoice(models.Model):
    task_code = models.ForeignKey(TaskCode, on_delete=models.DO_NOTHING)
    deal_amount = models.FloatField()
    paid_amount = models.FloatField()
    due_amount = models.FloatField()
    bill_file = models.FileField(upload_to='bills/', validators=[validate_file_extension])
    invoice_date = models.DateField()

    def __str__(self):
        return self.id

