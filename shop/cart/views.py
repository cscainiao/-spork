from json import dumps

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from cart.models import Goods


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'goods.html', {'goods_list': goods_list})


class CartItem(object):
    """购物车商品项"""
    def __init__(self, goods, amount=1):
        self.goods = goods
        self.amount = amount

    @property
    def total(self):
        return self.goods.price * self.amount


class ShoppingCart(object):
    """购物车类"""
    def __init__(self):
        self.num = 0
        self.items = {}

    def add_item(self, item):
        """添加商品"""
        if item.goods.id in self.items:
            self.items[item.goods.id].amount += item.amount
        else:
            self.items[item.goods.id] = item

    def remove_item(self, id):
        """移除商品"""
        if id in self.items:
            self.items.pop(id)

    def clear_all_items(self):
        """清空商品"""
        self.items.clear()

    @property
    def total(self):
        val = 0
        for item in self.items.values():
            val += item.total
        return val


def add_to_cart(request, id):
    goods = Goods.objects.get(pk=id)
    cart = request.session.get('cart', ShoppingCart())
    cart.add_item(CartItem(goods))
    request.session['cart'] = cart
    cart.num += 1
    return redirect('/')


def show_cart(request):
    cart = request.session.get('cart')
    cart_items = cart.items.values() if cart else []
    return render(request, 'cart.html', {'cart_items': cart_items, 'cart': cart})


def clear_items(request):
    cart = request.session.get('cart')
    cart.clear_all_items()
    request.session['cart'] = cart
    return redirect('/show_cart')


"""
def del_items(request, id):
    cart = request.session.get('cart')
    cart.remove_item(id)
    request.session['cart'] = cart
    return redirect('/show_cart')
"""

def del_items(request, id):
    cart = request.session.get('cart')
    cart.remove_item(id)
    request.session['cart'] = cart
    ctx ={'code': 200}
    return HttpResponse(dumps(ctx), content_type='application/json; charset=utf-8')