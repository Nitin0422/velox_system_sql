from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404




# Create your views here.
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_department_admin(user):
    return user.groups.filter(name='DepartmentAdmin').exists()

def is_staff(user):
    return user.groups.filter(name='Staff').exists()

@login_required(login_url='/')
def home(request):
    return render(request, 'temps/home.html', {})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('my_app:home')
        else:
            return render(request, 'temps/login.html', {"form": form})
    form = AuthenticationForm()
    return render(request, 'temps/login.html', {"form" : form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_app:home')
        else:
            print(form.error_messages)
            return render(request, 'temps/register.html', {"form": form})
    form = RegistrationForm()
    return render(request, 'temps/register.html', {'form' : form})

def logout_request(request):
    logout(request)
    return redirect('my_app:login')

def view_account_information(request):
    return render(request, 'temps/account-view.html', {})

@login_required(login_url='/')
def department_view(request):
    department_instances = []
    try:
        department_instances = get_list_or_404(Department)
    except:
        pass
    return render(request, 'temps/department/department_view.html', {"department_instances" : department_instances})

def department_add(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:department_view')
        else:
            return render(request, "temps/department/department_form.html", {"form": form})
    form = DepartmentForm()
    return render(request, "temps/department/department_form.html", {"form": form})

def department_edit(request, department_id):
    department_instance = get_object_or_404(Department, pk = department_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance = department_instance)
        if form.is_valid():
            form.save()
            return redirect('my_app:department_view')
        else:
            return render(request, "temps/department/department_form.html", {"form":form})
    form = DepartmentForm(instance= department_instance)
    return render(request, "temps/department/department_form.html", {"form":form})

def department_delete(request, department_id):
    department_instance = get_object_or_404(Department, pk = department_id)
    if request.method == "POST":
        department_instance.delete()
        return redirect('my_app:department_view')
    table_name = "Department"
    return render(request, "temps/confirm.html", {"instance": department_instance, "table_name" : table_name})


@login_required(login_url='/')
def task_category_view(request):
    task_category_instances = []
    try:
        task_category_instances = get_list_or_404(TaskCategory)
    except:
        pass
    return render(request, 'temps/task/task_category_view.html', {"task_category_instances" : task_category_instances})

def task_category_add(request):
    if request.method == "POST":
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:task_category_view')
        else:
            return render(request, "temps/task/task_category_form.html", {"form":form})
    form = TaskCategoryForm()
    return render(request, "temps/task/task_category_form.html", {"form":form})

def task_category_edit(request, task_category_id):
    task_category_instance = get_object_or_404(TaskCategory, pk = task_category_id)
    if request.method == "POST":
        form = TaskCategoryForm(request.POST, instance = task_category_instance)
        if form.is_valid():
            form.save()
            return redirect('my_app:task_category_view')
        else:
            return render(request, "temps/task/task_category_form.html", {"form" : form})
    form = TaskCategoryForm(instance= task_category_instance)
    return render(request, "temps/task/task_category_form.html", {"form" : form})

@login_required(login_url='/')
def department_groups_view(request):
    department_groups_instances = []
    try:
        department_groups_instances = get_list_or_404(DepartmentGroup)
    except:
        pass
    return render(request, 'temps/department/department_groups_view.html', {"department_groups_instances": department_groups_instances})

@login_required(login_url='/')
def employees_view(request):
    employee_instances = []
    try:
        employee_instances = get_list_or_404(Employee)
    except:
        pass
    return render(request, 'temps/employee/employees_view.html', {"employee_instances": employee_instances})

@login_required(login_url='/')
def customers_view(request):
    customer_instances = []
    try:
        customer_instances = get_list_or_404(Customer)
    except:
        pass
    return render(request, 'temps/customer/customers_view.html', {"customer_instances": customer_instances})

@login_required(login_url='/')
def tasks_view(request):
    tasks_instances = []
    try:
        tasks_instances = get_list_or_404(TaskCode)
    except:
        pass
    return render(request, 'temps/task/tasks_view.html', {"tasks_instances": tasks_instances})

@login_required(login_url='/')
def invoice_add(request):
    if request.method == 'POST':
        print("POST method is OK")
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            if is_admin(request.user):
                form.save()
            else:
                form_data = form.save(commit=False)
                form_data.employee_id = request.user.id
                form_data.save()
            print("The form is valid")
            return redirect('my_app:invoices_view')
        else:
            print("The form is not valid:  ")
            print(form.errors)
            return render(request, "temps/invoice_form.html", {"form": form})
    form = InvoiceForm()
    return render(request, 'temps/invoice/invoice_form.html', {"form": form})

@login_required(login_url='/')
def invoices_view(request):
    invoice_instances = []
    try:
        invoice_instances = get_list_or_404(Invoice)
    except:
        pass
    return render(request, 'temps/invoice/invoices_view.html', {"invoice_instances": invoice_instances})

@login_required(login_url='/')
def invoices_edit(request, invoice_id):
    try:
        invoice_instance = get_object_or_404(Invoice, pk = invoice_id)
        if request.method == 'POST':
            form = InvoiceForm(request.POST, instance = invoice_instance)
            if form.is_valid():
                form.save()
                return redirect('my_app:invoices_view')
            else:
                return render(request, "temps/invoice/invoice_form.html", {"form":form})
        form = InvoiceForm(instance = invoice_instance)
        return render(request, "temps/invoice/invoice_form.html", {"form":form})
    except:
        return redirect('my_app:invoices_view')
    
@login_required(login_url='/')
def invoices_delete(request, invoice_id):
    table_name = "Invoices"
    invoice_instance = get_object_or_404(Invoice, pk = invoice_id)
    if request.method == "POST":
        print("I am here")
        invoice_instance.delete()
        return redirect('my_app:invoices_view')
    return render(request, "temps/confirm.html", {"instance" : invoice_instance, "table_name" : table_name})

    








