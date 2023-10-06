def site_settings(request):
    return {"is_hr" : request.user.groups.filter(name = 'HR-Admin').exists(),
            "is_finance" : request.user.groups.filter(name = 'Finance-Admin').exists()}