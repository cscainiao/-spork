from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import Users


class UserAuthMiddle(MiddlewareMixin):

    def process_request(self, request):
        # 验证cookie中的tiket, 验证不通过,跳转到登录
        # 验证通过,request.user当前登录的用户信息

        path = request.path
        s = ['/user/login/', '/user/register/']
        if path in s:
            return None
        ticket = request.COOKIES.get('ticket')

        if not ticket:
            return HttpResponseRedirect(reverse('login'))

        user = Users.objects.filter(ticket=ticket)

        if not user:
            return HttpResponseRedirect(reverse('login'))

        request.user = user