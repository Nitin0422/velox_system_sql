from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, InvoiceForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.shortcuts import get_list_or_404




# Create your views here.
def is_hr(user):
    return user.groups.filter(name='HR-Admin').exists()

def is_finance(user):
    return user.groups.filter(name='Finance-Admin').exists()

@login_required(login_url='/')
def home(request):
    return render(request, 'temps/home.html', {})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data.get('username')
            print(username)
            password = form.cleaned_data.get('password')
            print(password)
            user = authenticate(username = username, password = password)
            print("User is: ", user)
            if user is not None:
                login(request, user)
                print("Logged in hai")
                return redirect('my_app:home')
    form = AuthenticationForm()
    return render(request, 'temps/login.html', {"form" : form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_app:home')
    form = RegistrationForm()
    return render(request, 'temps/register.html', {'form' : form})

def logout_request(request):
    logout(request)
    return redirect('my_app:login')

@login_required(login_url='/')
def view_data(request):
    return render(request, 'temps/view_data.html', {})

@login_required(login_url='/')
def add_data(request):
    return render(request, 'temps/add_data.html', {})


@login_required(login_url='/')
def department_view(request):
    department_instances = []
    try:
        department_instances = get_list_or_404(Department)
    except:
        pass
    return render(request, 'temps/department_view.html', {"department_instances" : department_instances})

@login_required(login_url='/')
def task_category_view(request):
    task_category_instances = []
    try:
        task_category_instances = get_list_or_404(TaskCategory)
    except:
        pass
    return render(request, 'temps/task_category_view.html', {"task_category_instances" : task_category_instances})

@login_required(login_url='/')
def department_groups_view(request):
    department_groups_instances = []
    try:
        department_groups_instances = get_list_or_404(DepartmentGroup)
    except:
        pass
    return render(request, 'temps/department_groups_view.html', {"department_groups_instances": department_groups_instances})

@login_required(login_url='/')
def employees_view(request):
    employee_instances = []
    try:
        employee_instances = get_list_or_404(Employee)
    except:
        pass
    return render(request, 'temps/employees_view.html', {"employee_instances": employee_instances})

@login_required(login_url='/')
def customers_view(request):
    customer_instances = []
    try:
        customer_instances = get_list_or_404(Customer)
    except:
        pass
    return render(request, 'temps/customers_view.html', {"customer_instances": customer_instances})

@login_required(login_url='/')
def tasks_view(request):
    tasks_instances = []
    try:
        tasks_instances = get_list_or_404(TaskCode)
    except:
        pass
    return render(request, 'temps/tasks_view.html', {"tasks_instances": tasks_instances})

@login_required(login_url='/')
def invoice_add(request):
    if request.method == 'POST':
        print("POST method is OK")
        form = InvoiceForm(request.POST, request.FILES)  # Populate the form with POST data
        print("The form is being made ?")
        if form.is_valid():
            form.save()
            return redirect('my_app:invoices_view')
            print("The form is valid")
            # Form is valid, print the data collected from the frontend
            for key, value in form.cleaned_data.items():
                print(f'{key}: {value}')
        else:
            print("The form is not valid:  ")
            print(form.errors)
    form = InvoiceForm()
    return render(request, 'temps/invoice_form.html', {"form": form})

@login_required(login_url='/')
def invoices_view(request):
    invoice_instances = []
    try:
        invoice_instances = get_list_or_404(Invoice)
    except:
        pass
    return render(request, 'temps/invoices_view.html', {"invoice_instances": invoice_instances})








