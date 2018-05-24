from django.urls import path

from hrs import views

# 在django 1.x的版本中url('depts/emps/(?P<no>[0-9]+)', views.emps, name='empsindept'),
# 来获取emps后面的no

urlpatterns = [
    path('depts', views.depts, name='depts'),
    # path('depts/emps', views.emps, name='empsindept'),
    path('depts/emps/<int:dno>', views.emps, name='empsindept'),
    path('deldept/<int:dno>', views.del_dept, name='ddel')
]