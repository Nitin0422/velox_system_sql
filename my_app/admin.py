from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(DepartmentGroup)
admin.site.register(Employee)
admin.site.register(EmployeeAssociation)
admin.site.register(Customer)
admin.site.register(TaskCategory)
admin.site.register(TaskCode)
admin.site.register(Invoice)
