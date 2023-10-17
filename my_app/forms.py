from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Invoice, Employee, Department, TaskCategory, TaskCode, Customer, DepartmentGroup

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('username', 'password1', 'password2')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_name', 'no_of_employees')

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = ['task_category_name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskCode
        fields = ['task_category', 'task_code_name']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['task_category'].widget.attrs.update({'class':'form-select'})

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_full_name', 'customer_phone_number', 'customer_address']

class DepartmentGroupForm(forms.ModelForm):
    class Meta:
        model = DepartmentGroup
        fields = ['department', 'group_name']

    def __init__(self, *args, **kwargs):
        super(DepartmentGroupForm, self).__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update({'class' : 'form-select'})
  
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'task_category', 'employee','task_code', 'deal_amount', 'paid_amount', 'due_amount', 'bill_file', 'invoice_date' ]

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['task_code'].widget.attrs.update({'class': 'form-select'})
        self.fields['customer'].widget.attrs.update({'class': 'form-select'})
        self.fields['task_category'].widget.attrs.update({'class': 'form-select'})
        self.fields['employee'].widget.attrs.update({'class':'form-select'})
    

