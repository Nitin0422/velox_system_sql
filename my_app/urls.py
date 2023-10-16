from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('account/', views.view_account_information, name='account_information'),
    path('', views.login_request, name='login'),
    path('register/', views.register, name ='register'),
    path('logout/', views.logout_request, name='logout'),

    path('department/', views.department_view, name='department_view'),
    path('department/add/', views.department_add, name='department_add'),

    path('task-category/', views.task_category_view, name= 'task_category_view'),

    path('department/groups/', views.department_groups_view, name='department_groups_view'),
    path('department/employees/', views.employees_view, name='employees_view'),

    path('customers/', views.customers_view, name='customers_view'),
    path('tasks/', views.tasks_view, name='tasks_view'),

    path('invoice/add', views.invoice_add, name='invoice_add'),
    path('invoices/', views.invoices_view, name='invoices_view'),
    path('invoices/edit/<int:invoice_id>', views.invoices_edit, name="invoices_edit"),
    path('invoices/delete/<int:invoice_id>', views.invoices_delete, name="invoices_delete"),    
]
