from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('item1', views.item1, name='item1'),
    path('item2', views.item2, name='item2'),

    path('mega-section-1/item11', views.mega_section_1_item11, name='mega1-sec1-item11'),
    path('mega-section-1/item12', views.mega_section_1_item12, name='mega1-sec1-item12'),
    path('mega-section-1/item13', views.mega_section_1_item13, name='mega1-sec1-item13'),

    path('mega-section-1/item21', views.mega_section_1_item21, name='mega1-sec2-item21'),
    path('mega-section-1/item22', views.mega_section_1_item22, name='mega1-sec2-item22'),
    path('mega-section-1/item23', views.mega_section_1_item23, name='mega1-sec2-item23'),

    path('mega-section-1/item31', views.mega_section_1_item31, name='mega1-sec3-item31'),
    path('mega-section-1/item32', views.mega_section_1_item32, name='mega1-sec3-item32'),
    path('mega-section-1/item33', views.mega_section_1_item33, name='mega1-sec3-item33'),

    path('mega-section-2/item11', views.mega_section_2_item11, name='mega2-sec1-item11'),
    path('mega-section-2/item12', views.mega_section_2_item12, name='mega2-sec1-item12'),
    path('mega-section-2/item13', views.mega_section_2_item13, name='mega2-sec1-item13'),

    path('mega-section-2/item21', views.mega_section_2_item21, name='mega2-sec2-item21'),
    path('mega-section-2/item22', views.mega_section_2_item22, name='mega2-sec2-item22'),
    path('mega-section-2/ite23', views.mega_section_2_item23, name='mega2-sec2-item23'),

    path('mega-section-2/item31', views.mega_section_2_item31, name='mega2-sec3-item31'),
    path('mega-section-2/item32', views.mega_section_2_item32, name='mega2-sec3-item32'),
    path('mega-section-2/item33', views.mega_section_2_item33, name='mega2-sec3-item33'),

    path('mega-section-3/item11', views.mega_section_3_item11, name='mega3-sec1-item11'),
    path('mega-section-3/item12', views.mega_section_3_item12, name='mega3-sec1-item12'),
    path('mega-section-3/item13', views.mega_section_3_item13, name='mega3-sec1-item13'),

    path('mega-section-3/item21', views.mega_section_3_item21, name='mega3-sec2-item21'),
    path('mega-section-3/item22', views.mega_section_3_item22, name='mega3-sec2-item22'),
    path('mega-section-3/item23', views.mega_section_3_item23, name='mega3-sec2-item23'),

    path('mega-section-3/item31', views.mega_section_3_item31, name='mega3-sec3-item31'),
    path('mega-section-3/item32', views.mega_section_3_item32, name='mega3-sec3-item32'),
    path('mega-section-3/item33', views.mega_section_3_item33, name='mega3-sec3-item33'),
]
