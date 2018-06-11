# from django.urls import path
from django.conf.urls import url

from user import views

urlpatterns = [
    #django自带实现
    # path('djlogout/', views.djlogout, name='djlogout'),
    # path('djlogin/', views.djlogin, name='djlogin'),
    # path('djregister/', views.djregister, name='djregister'),

    #自己写方法实现
    url(r'logout/', views.logout, name='logout'),
    url(r'login/', views.login, name='login'),
    url('register/', views.register, name='register'),

    #权限
    url(r'userper/', views.userper),
]