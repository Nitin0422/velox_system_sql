from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def is_hr(request):
    return request.user.groups.filter(name='HR-Admin').exists()

def is_finance(request):
    return request.user.groups.filter(name='Finance-Admin').exists()

def home(request):
    return render(request, 'temps/home.html', {})

def login(request):
    return render(request, 'temps/login.html', {})

def item1(request):
    return render(request, 'temps/item1.html', {})

def item2(request):
    return render(request, 'temps/item2.html', {})

def mega_section_1_item11(request):
    return render(request, 'temps/mega-section-1/item11.html', {})

def mega_section_1_item12(request):
    return render(request, 'temps/mega-section-1/item12.html', {})

def mega_section_1_item13(request):
    return render(request, 'temps/mega-section-1/item11.html', {})

def mega_section_1_item21(request):
    return render(request, 'temps/mega-section-1/item21.html', {})

def mega_section_1_item22(request):
    return render(request, 'temps/mega-section-1/item22.html', {})

def mega_section_1_item23(request):
    return render(request, 'temps/mega-section-1/item21.html', {})

def mega_section_1_item31(request):
    return render(request, 'temps/mega-section-1/item31.html', {})

def mega_section_1_item32(request):
    return render(request, 'temps/mega-section-1/item32.html', {})

def mega_section_1_item33(request):
    return render(request, 'temps/mega-section-1/item31.html', {})

@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item11(request):
    return render(request, 'temps/mega-section-2/item11.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item12(request):
    return render(request, 'temps/mega-section-2/item12.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item13(request):
    return render(request, 'temps/mega-section-2/item11.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item21(request):
    return render(request, 'temps/mega-section-2/item21.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item22(request):
    return render(request, 'temps/mega-section-2/item22.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item23(request):
    return render(request, 'temps/mega-section-2/item21.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item31(request):
    return render(request, 'temps/mega-section-2/item31.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item32(request):
    return render(request, 'temps/mega-section-2/item32.html', {})
@user_passes_test(is_hr, login_url= '/')
def mega_section_2_item33(request):
    return render(request, 'temps/mega-section-2/item31.html', {})

@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item11(request):
    return render(request, 'temps/mega-section-3/item11.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item12(request):
    return render(request, 'temps/mega-section-3/item12.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item13(request):
    return render(request, 'temps/mega-section-3/item11.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item21(request):
    return render(request, 'temps/mega-section-3/item21.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item22(request):
    return render(request, 'temps/mega-section-3/item22.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item23(request):
    return render(request, 'temps/mega-section-3/item21.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item31(request):
    return render(request, 'temps/mega-section-3/item31.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item32(request):
    return render(request, 'temps/mega-section-3/item32.html', {})
@user_passes_test(is_finance, login_url= '/')
def mega_section_3_item33(request):
    return render(request, 'temps/mega-section-3/item31.html', {})


