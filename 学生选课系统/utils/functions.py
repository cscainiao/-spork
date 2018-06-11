#定义装饰器
from django.http import HttpResponseRedirect
from django.urls import reverse
from user.models import Users




def is_login(func):
    def check_login(request):
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('login'))
        user = Users.objects.filter(ticket=ticket)
        if not user:
            return HttpResponseRedirect(reverse('login'))
        return func(request)
    return check_login



