def site_settings(request):
    is_hr = False
    is_finance = False
    
    if request.user.is_authenticated:
        is_hr = request.user.groups.filter(name='HR-Admin').exists()
        is_finance = request.user.groups.filter(name='Finance-Admin').exists()

    return {
        "is_hr": is_hr,
        "is_finance": is_finance
    }