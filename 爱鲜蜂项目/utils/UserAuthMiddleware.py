from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import UserTicketModel


class UserAuthMiddle(MiddlewareMixin):

    def process_request(self, request):
        # 个人中心 商品增加删除  购物车
        need_login = ['/axf/mine/', '/axf/addCart/', '/axf/delCart/', '/axf/cart/', '/axf/selectAll/',
                      '/axf/changeCartState/', '/axf/showMoney/', '/axf/pay/', '/axf/clearAll/',
                      '/axf/orderListWaitPay/', '/axf/orderListPayed/',
                      ]
        if request.path in need_login:
            ticket = request.COOKIES.get('ticket')
            if not ticket:
                return HttpResponseRedirect(reverse('user:login'))
            user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
            if user_ticket:
                if datetime.utcnow() > user_ticket.out_time.replace(tzinfo=None):
                    UserTicketModel.objects.filter(user=user_ticket.user).delete()
                    return HttpResponseRedirect(reverse('user:login'))
                else:
                    request.user = user_ticket.user
                    UserTicketModel.objects.filter(Q(user=user_ticket.user) & ~Q(ticket=ticket)).delete()

            else:
                return HttpResponseRedirect(reverse('user:login'))

        else:
            return None