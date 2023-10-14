def site_settings(request):
    is_admin = False
    is_department_admin =False
    is_staff = False
    
    
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='Admin').exists()
        is_department_admin = request.user.groups.filter(name="DepartmentAdmin").exists()
        is_staff = request.user.groups.filter(name = "Staff").exists()

    return {
        "is_admin": is_admin,
        "is_department_admin": is_department_admin,
        "is_staff": is_staff
    }