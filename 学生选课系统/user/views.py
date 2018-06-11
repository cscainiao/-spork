import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.models import Users, Role

"""
django自带的登录注册注销
def djlogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username, password=password)
        if User:
            return HttpResponseRedirect(reverse('index'))
        else:
            msg = '用户名或者密码错误'
            return render(request, 'login.html', {'msg': msg})


def djlogout(request):
    if request.method == 'GET':
        auth.logout(request)
    return HttpResponseRedirect(reverse('djlogin'))


def djregister(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        user_name = request.POST['user_name']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        if not all([user_name, pwd1, pwd2]):
            msg = '请填写所有参数'
            return render(request, 'register.html', {'msg': msg})

        if pwd1 != pwd2:
            msg = '两次密码不一致'
            return render(request, 'register.html', {'msg': msg})

        User.objects.create_user(username=user_name, password=pwd1)

        return HttpResponseRedirect(reverse('djregister'))
"""


# 自己手动实现
def register(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        user_name = request.POST['user_name']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        if not all([user_name, pwd1, pwd2]):
            msg = '请填写所有参数'
            return render(request, 'register.html', {'msg': msg})

        if pwd1 != pwd2:
            msg = '两次密码不一致'
            return render(request, 'register.html', {'msg': msg})

        Users.objects.create(username=user_name, password=pwd1)

        return HttpResponseRedirect(reverse('register'))


def login(request):
    """登录"""
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = Users.objects.filter(username=username, password=password).first()
        if user:
            s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            ticket = ''
            for i in range(28):
                ticket += random.choice(s)
            user.ticket = ticket
            user.save()
            response = HttpResponseRedirect(reverse('index'))
            response.set_cookie('ticket', ticket)
            return response
        else:
            msg = '用户名或者密码错误'
            return render(request, 'login.html', {'msg': msg})


def logout(request):
    """注销"""
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('login'))
        response.delete_cookie('ticket')
        return response


def userper(request):
    # 查询妲己有哪些权限
    # 妲己 角色 权限
    user = Users.objects.filter(username='妲己').first()
    # user和role一对一的关系得到user直接.role就可以得到role对象
    #若果的一对多就要.role_set得到所有的对象
    u_r_p = user.role.r_p.all()                                              #要理解

    # 判断妲己是否有学生列表的权限 exists()判断是否存在
    u_r_p.filter(p_en='STULIST').exists()

