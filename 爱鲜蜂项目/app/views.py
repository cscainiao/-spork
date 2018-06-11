from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from app.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods, CartModel, OrderModel, \
    OrderGoodsModel
from user.models import UserModel, UserTicketModel
from utils.functions import total_money, get_order_random_id


def home(request):
    """
    首页视图
    """
    if request.method == 'GET':
        mainwheels = MainWheel.objects.all()
        mainnav = MainNav.objects.all()
        mustbuy = MainMustBuy.objects.all()
        shops = MainShop.objects.all()
        mainshows = MainShow.objects.all()
        data = {
            'title': '首页',
            'mainwheels': mainwheels,
            'mainnav': mainnav,
            'mustbuy': mustbuy,
            'shops': shops,
            'mainshows': mainshows
        }
        return render(request, 'home/home.html', data)


def mine(request):
    """
    我的
    """
    if request.method == 'GET':
        user = request.user
        user_orders = OrderModel.objects.filter(user=user)
        wait_pay, already_pay = 0, 0
        for user_order in user_orders:
            if user_order.o_status == 0:
                wait_pay += 1
            if user_order.o_status == 1:
                already_pay += 1
        data = {
            'wait_pay': wait_pay,
            'already_pay': already_pay
        }
        return render(request, 'mine/mine.html', data)


def cart(request):
    """
    购物车
    """
    if request.method == 'GET':
        user = request.user
        user_carts = CartModel.objects.filter(user=user)
        data = {
            'user_carts': user_carts
        }

        return render(request, 'cart/cart.html', data)


def market(request):
    """
    闪购
    """
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('app:user_market', args=('104749', '0', '0')))


def user_market(request, typeid, cid, sid):
    """
    闪购页面详情
    :param typeid: 左侧分类id
    :param cid: 子分类(全部分类id)
    :param sid: 排序id
    """
    if request.method == 'GET':
        foodtypes = FoodType.objects.all()

        '''点击全部分类信息的单一分类后, 显示当前分类的商品'''
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        else:
            goods = Goods.objects.filter(categoryid=typeid, childcid=cid)

        '''排序'''
        if sid == '0':
            pass
        if sid == '1':
            goods = goods.order_by('-productnum')
        if sid == '2':
            goods = goods.order_by('-price')
        if sid == '3':
            goods = goods.order_by('price')

        '''显示分类信息'''
        #获取当前类别
        foodtypes_current = foodtypes.filter(typeid=typeid).first()
        if foodtypes_current:
            #当前类别下面的全部分类
            childtype = foodtypes_current.childtypenames
            childtypename = childtype.split('#')
            child_list = []
            for i in childtypename:
                a = i.split(':')
                child_list.append(a)

            data = {
                'foodtypes': foodtypes,
                'goods': goods,
                'typeid': typeid,
                'foodtypes_current': foodtypes_current,
                'child_list': child_list,
                'cid': cid,
            }
            return render(request, 'market/market.html', data)


def addCart(request):
    """
    增加购物车
    """
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST['goods_id']
        data = {
            'code': 200,
            'msg': '请求成功',
        }
        if user.id:
            user_carts = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num


            else:
                CartModel.objects.create(user=user, goods_id=goods_id)
                data['c_num'] = 1

            totalMoney = total_money(user)
            data['totalMoney'] = totalMoney
            return JsonResponse(data)

        data['code'] = 403
        data['msg'] = '用户未登录'

        return JsonResponse(data)


def delCart(request):
    """
    删除购物车
    """
    if request.method == 'POST':
        user = request.user
        # 1. 先拿到isselect为True的购物车, 在拿到购物车下面商品的数量和单价
        goods_id = request.POST['goods_id']
        data = {
            'code': 200,
            'msg': '请求成功',
        }
        if user.id:
            user_cart = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            if user_cart:
                if user_cart.c_num == 1:
                    user_cart.delete()
                    data['c_num'] = 0
                if user_cart.c_num > 1:
                    user_cart.c_num -= 1
                    user_cart.save()
                    data['c_num'] = user_cart.c_num
            else:
                pass


            totalMoney = total_money(user)
            data['totalMoney'] = totalMoney
            return JsonResponse(data)
        data['msg'] = '请登录'
        return JsonResponse(data)


def changeCartState(request):
    """
    改变购物车的状态
    """
    if request.method == 'POST':
        user = request.user
        cart_id = request.POST['cart_id']
        user_cart = CartModel.objects.filter(id=cart_id).first()

        if user_cart.is_select:
            user_cart.is_select = False

        else:
            user_cart.is_select = True

        user_cart.save()

        data = {
            'code': 200,
            'msg': '请求成功',
            'is_select': user_cart.is_select
        }
        totalMoney = total_money(user)
        data['totalMoney'] = totalMoney
        return JsonResponse(data)


def selectAll(request):
    """
    全选
    """
    if request.method == 'POST':
        user = request.user
        user_carts = user.cartmodel_set.all()

        for user_cart in user_carts:
            user_cart.is_select = True

            user_cart.save()

        data = {
            'code': 200,
            'msg': '请求成功',
        }
        totalMoney = total_money(user)
        data['totalMoney'] = totalMoney
        return JsonResponse(data)

def clearAll(request):
    """
    全选
    """
    if request.method == 'POST':
        user = request.user
        user_carts = user.cartmodel_set.all()

        for user_cart in user_carts:
            user_cart.is_select = False
            user_cart.save()
        data = {
            'code': 200,
            'msg': '请求成功',
        }
        totalMoney = total_money(user)
        data['totalMoney'] = totalMoney
        return JsonResponse(data)


def showMoney(request):
    """
    购物车页面get请求时自动加载总价
    """
    user = request.user
    totalMoney = total_money(user)
    data = {'totalMoney': totalMoney}
    return JsonResponse(data)


def pay(request):
    """
    下单
    """
    if request.method == 'GET':
        user = request.user
        # 创建订单
        o_num = get_order_random_id()
        order = OrderModel.objects.create(user=user, o_num=o_num)
        # 选择勾选的商品下单
        user_carts = CartModel.objects.filter(user=user, is_select=True)
        for carts in user_carts:
            OrderGoodsModel.objects.create(goods=carts.goods,
                                           order=order,
                                           goods_num=carts.c_num
                                           )

        user_carts.delete()

        return render(request, 'order/order_info.html', {'order': order, 'user_carts': user_carts})


def alipay(request):
    """
    支付
    """
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = OrderModel.objects.filter(id=order_id).first()
        order.o_status = 1
        order.save()
        return JsonResponse({'code': 200, 'msg': '支付成功'})


def orderListWaitPay(request):
    """
    代付款
    """
    if request.method == 'GET':
        user = request.user
        user_orders = OrderModel.objects.filter(user=user, o_status=0)

        return render(request, 'order/order_list_wait_pay.html', {'user_orders': user_orders})


def orderListPayed(request):
    """
    待收货
    """
    if request.method == 'GET':
        user = request.user
        user_orders = OrderModel.objects.filter(user=user, o_status=1)
        return render(request, 'order/order_list_payed.html', {'user_orders': user_orders})


def confirmGoods(request, order_id):
    """
    确认收货
    """
    if request.method == 'GET':
        order = OrderModel.objects.filter(id=order_id).first()
        order.o_status = 3
        order.save()
        return HttpResponseRedirect(reverse('app:mine'))


def waitPay(request, order_id):
    """
    代付款里面的支付
    """
    if request.method == 'GET':
        order = OrderModel.objects.filter(id=order_id).first()
        order.o_status = 1
        order.save()
        return HttpResponseRedirect(reverse('app:mine'))