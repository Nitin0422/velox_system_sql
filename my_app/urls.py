from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_request, name='login'),
    path('register/', views.register, name ='register'),
    path('logout/', views.logout_request, name='logout'),

    path('view-data/', views.view_data, name='view_data'),
    path('add-data/', views.add_data, name='add_data'),

    
]
