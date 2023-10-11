from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=200)
    no_of_employees = models.IntegerField()

class DepartmentGroup(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(DepartmentGroup, on_delete=models.DO_NOTHING)
    employee_full_name = models.CharField(max_length=200)
    employee_contact_number = models.CharField(max_length=200)
    employee_address = models.CharField(max_length=200)
    employee_PAN = models.CharField(max_length=200)
    email = models.EmailField()

class Customer(models.Model):
    customer_full_name = models.CharField(max_length=200)
    customer_phone_number = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)

class TaskCategory(models.Model):
    task_category_name = models.CharField(max_length=200)

class TaskCode(models.Model):
    task_category = models.ForeignKey(TaskCategory, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    task_date = models.DateField()

class Invoice(models.Model):
    task_code = models.ForeignKey(TaskCode, on_delete=models.DO_NOTHING)
    deal_amount = models.FloatField()
    paid_amount = models.FloatField()
    due_amount = models.FloatField()
    bill_file = models.FileField()
    invoice_date = models.DateField()



