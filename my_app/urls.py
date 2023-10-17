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
    path('department/edit/<int:department_id>', views.department_edit, name="department_edit" ),
    path('department/delete/<int:department_id>', views.department_delete, name="department_delete"),

    path('task-category/', views.task_category_view, name= 'task_category_view'),
    path('task-category/add', views.task_category_add, name="task_category_add"),
    path('task-category/edit/<int:task_category_id>', views.task_category_edit, name = 'task_category_edit'),
    path('task-category/delete/<int:task_category_id>', views.task_category_delete, name="task_category_delete"),

    path('tasks/', views.tasks_view, name='tasks_view'),
    path('tasks/add', views.tasks_add, name = "tasks_add"),
    path('tasks/edit/<int:task_code_id>', views.tasks_edit, name="tasks_edit"),
    path('tasks/delete/<int:task_code_id>', views.tasks_delete, name="tasks_delete"),

    path('department/groups/', views.department_groups_view, name='department_groups_view'),
    path('department/groups/add', views.department_groups_add, name = "department_groups_add"),
    path('department/groups/edit/<int:department_group_id>', views.department_groups_edit, name="department_groups_edit"),
    path('department/groups/delete/<int:department_group_id>', views.department_groups_delete, name='department_groups_delete'),

    path('department/employees/', views.employees_view, name='employees_view'),
    path('department/employees/add', views.employees_add, name="employees_add"),
    path('department/employees/edit/<int:employee_id>', views.employees_edit, name = "employees_edit"),
    path('department/employees/delete/<int:employee_id>', views.employees_delete, name="employees_delete"),

    path('customers/', views.customers_view, name='customers_view'),
    path('customer/add/', views.customer_add, name='customers_add'),
    path('customer/edit/<int:customer_id>', views.customer_edit, name='customers_edit'),
    path('customer/delete/<int:customer_id>', views.customer_delete, name='customers_delete'),

    path('invoice/add', views.invoice_add, name='invoice_add'),
    path('invoices/', views.invoices_view, name='invoices_view'),
    path('invoices/edit/<int:invoice_id>', views.invoices_edit, name="invoices_edit"),
    path('invoices/delete/<int:invoice_id>', views.invoices_delete, name="invoices_delete"),    
]
