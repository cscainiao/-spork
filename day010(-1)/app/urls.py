from django.urls import path

from app import views

#可以使用django自带的login_required来对每个页面要求登录了才能访问
#或者一般使用中间件来对url进行过滤 setting里面的MIDDLEWARE
urlpatterns = [
    path('index/', views.index, name='index'),
    path('left/', views.left, name='left'),
    path('grade/', views.grade, name='grade'),
    path('head/', views.head, name='head'),
    path('addgrade/', views.addgrade, name='addgrade'),
    path('addstu/', views.addstu, name='addstu'),
    path('student/', views.student, name='student'),
    path('student/del_stu/<int:id>', views.del_stu, name='del_stu'),
    path('editgrade/', views.editgrade, name='editgrade'),
]