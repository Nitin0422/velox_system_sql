from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm





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
    return render(request, 'temps/department_view.html', {})

@login_required(login_url='/')
def task_category_view(request):
    return render(request, 'temps/task_category_view.html', {})

@login_required(login_url='/')
def department_groups_view(request):
    return render(request, 'temps/department_groups_view.html', {})

@login_required(login_url='/')
def employees_view(request):
    return render(request, 'temps/employees_view.html', {})

@login_required(login_url='/')
def customers_view(request):
    return render(request, 'temps/customers_view.html', {})

@login_required(login_url='/')
def tasks_view(request):
    return render(request, 'temps/tasks_view.html', {})

@login_required(login_url='/')
def invoice_add(request):
    return render(request, 'temps/invoice_add.html', {})

@login_required(login_url='/')
def invoices_view(request):
    return render(request, 'temps/invoices_view.html', {})








