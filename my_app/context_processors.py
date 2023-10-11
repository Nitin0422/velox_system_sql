def site_settings(request):
    is_admin = False
    
    
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='Admin').exists()

    return {
        "is_admin": is_admin,
    }