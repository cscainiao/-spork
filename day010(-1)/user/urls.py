from django.urls import path

from user import views

urlpatterns = [
    #django自带实现
    # path('djlogout/', views.djlogout, name='djlogout'),
    # path('djlogin/', views.djlogin, name='djlogin'),
    # path('djregister/', views.djregister, name='djregister'),

    #自己写方法实现
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]