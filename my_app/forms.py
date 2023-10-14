from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Invoice, Staff

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'PAN', 'email', 'username', 'password1', 'password2')
  
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['task_code', 'deal_amount', 'paid_amount', 'due_amount', 'bill_file', 'invoice_date' ]

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['task_code'].widget.attrs.update({'class': 'form-select'})
    

