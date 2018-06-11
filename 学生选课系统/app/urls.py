# from django.urls import path
from django.conf.urls import url

from app import views
from rest_framework.routers import SimpleRouter


# api
router = SimpleRouter()
router.register('api/student', views.api_student)
router.register('api/grade', views.api_grade)

#可以使用django自带的login_required来对每个页面要求登录了才能访问
#或者一般使用中间件来对url进行过滤 setting里面的MIDDLEWARE
#或者自己定义一个装饰器类似于login_required
urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'left/', views.left, name='left'),
    url(r'grade/', views.grade, name='grade'),
    url(r'head/', views.head, name='head'),
    url(r'addgrade/', views.addgrade, name='addgrade'),
    url(r'addstu/', views.addstu, name='addstu'),
    url(r'student/', views.student, name='student'),
    # url(r'student/del_stu/<int:id>', views.del_stu, name='del_stu'),
    url(r'editgrade/', views.editgrade, name='editgrade'),
    url(r'editgradebyapi/', views.editgradebyapi, name='editgradebyapi'),


    # F/Q
    url('select/', views.select),
]

urlpatterns += router.urls