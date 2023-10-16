from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Invoice, Employee, Department

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('username', 'password1', 'password2')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_name', 'no_of_employees')
  
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
    

