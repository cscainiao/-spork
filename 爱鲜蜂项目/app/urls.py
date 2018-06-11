from django.conf.urls import url

from app import views

urlpatterns = [
    # 主页
    url(r'^home/', views.home, name='home'),
    # 个人中心
    url(r'^mine/', views.mine, name='mine'),

    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # 闪购
    url(r'^market/$', views.market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.user_market, name='user_market'),

    # 添加购物车
    url(r'^addCart/', views.addCart, name='addCart'),
    # 删除购物车
    url(r'^delCart/', views.delCart, name='delCart'),

    # 改变购物车里面的状态(钩钩xx)
    url(r'^changeCartState/', views.changeCartState, name='changeCartState'),
    # 全选
    url(r'^selectAll/', views.selectAll, name='selectAll'),
    # 取消全选
    url(r'^clearAll/', views.clearAll, name='clearAll'),
    # 购物车页面get请求时自动加载总价
    url(r'^showMoney/', views.showMoney),

    # 下单
    url(r'^pay/', views.pay, name='pay'),
    # 支付
    url(r'^alipay/', views.alipay, name='alipay'),
    # 代付款
    url(r'^orderListWaitPay/', views.orderListWaitPay, name='orderListWaitPay'),
    # 待收货
    url(r'^orderListPayed/', views.orderListPayed, name='orderListPayed'),

    # 代付款 待收货 的付款收货
    url(r'^waitPay/(\d+)/', views.waitPay, name='waitPay'),
    url(r'^confirmGoods/(\d+)/', views.confirmGoods, name='confirmGoods'),
]