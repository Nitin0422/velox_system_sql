from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Invoice

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return user
    
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['task_code', 'deal_amount', 'paid_amount', 'due_amount', 'bill_file', 'invoice_date' ]
        
    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['task_code'].widget.attrs.update({'class': 'form-select'})
    

