from datetime import datetime, timedelta
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from django.urls import reverse

from user.models import UserModel, UserTicketModel


def login(request):
    """
    登录
    """
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserModel.objects.filter(username=username).first()
        if user:
            if check_password(password, user.pwd):
                s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
                ticket = ''
                for i in range(28):
                    ticket += random.choice(s)
                UserTicketModel.objects.create(user=user, ticket=ticket)
                response = HttpResponseRedirect(reverse('app:mine'))
                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket', ticket, expires=out_time)
                return response
            else:
                msg = '用户名或者密码错误'
                return render(request, 'user/user_login.html', {'msg': msg})
        else:
            msg = '用户名或者密码错误'
            return render(request, 'user/user_login.html', {'msg': msg})


def logout(request):
    """
    注销
    """
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('user:login'))
        response.delete_cookie('ticket')
        return response


def register(request):
    """
    注册
    """
    if request.method == 'GET':
        return render(request, 'user/user_register.html')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)
        icon = request.FILES.get('icon')
        password_confirm = request.POST['password_confirm']
        if not all([username, email, password, password_confirm]):
            msg = '请填写所有参数'
            return render(request, 'user/user_register.html', {'msg': msg})
        UserModel.objects.create(username=username, pwd=password, enmail=email, icon=icon)
        return HttpResponseRedirect(reverse('user:login'))

