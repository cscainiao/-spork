from json import dumps

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from hrs.models import Dept, Emp


def home(request):
    txc = {
        'hello': 'hello world, and bitch'
    }
    return render(request, 'index.html', txc)

def del_dept(request, dno):
    # dno = int(request.GET['dno'])

    dept = Dept.objects.get(pk=dno)
    # python中try except 优于if else
    try:
        dept.delete()
        ctx = {
            'code': 200
        }
    except:
        ctx = {
            'code': 404
        }
    return HttpResponse(
        dumps(ctx), content_type='application/json; charset=utf-8'
    )
    # 重定向-重新请求一个指定的页面
    # return redirect(reverse('depts'))

def emps(request, dno):
    # request.META返回浏览器请求头字典
    # request.get返回url?后面的构造地址的字典
    # dno = int(request.GET['dno'])
    # 查询员工外键约束的部门标号和请求地址的部门编号一样的列表 select_related 连接查询
    # QuerySet 使用了惰性查询,如果不是非要得到数据就不查询 这样可以节省服务器内存使用
    emps_list = list(Emp.objects.filter(dept__dno=dno).select_related('dept'))
    ctx = {
        'emps_list': emps_list,
        'dept_name': emps_list[0].dept.name
    } if len(emps_list) > 0 else {}
    return render(request, 'emps.html', ctx)


def depts(request):
    ctx={
    'dept_list': Dept.objects.all()
    }
    return render(request, 'dept.html', context=ctx)