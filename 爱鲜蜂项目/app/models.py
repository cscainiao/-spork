from django.db import models

from user.models import UserModel


class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=16)  #订单编号

    class Meta:
        abstract = True


#轮播
class MainWheel(Main):
    class Meta:
        db_table = "axf_wheel"


#导航
class MainNav(Main):
    class Meta:
        db_table = "axf_nav"


# 必购
class MainMustBuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


# 商店
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'


# 主页展示
class MainShow(Main):
    categoryid = models.CharField(max_length=16)  # category分类
    brandname = models.CharField(max_length=100)    # brand品牌

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_mainshow'


#食物分类
class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = "axf_foodtypes"


# 商品类
class Goods(models.Model):
    productid = models.CharField(max_length=16)
    productimg = models.CharField(max_length=200) #商品图片
    productname = models.CharField(max_length=100) #商品名称
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)
    price = models.FloatField(default=0)        #现价
    marketprice = models.FloatField(default=1)  #商场价
    categoryid = models.CharField(max_length=16) #左侧分类id
    childcid = models.CharField(max_length=16) #全部分类下面的子分类
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=16)
    storenums = models.IntegerField(default=1)
    productnum = models.IntegerField(default=1)  #销量

    class Meta:
        db_table = "axf_goods"


class CartModel(models.Model):    # 购物车
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(Goods)    # 关联商品
    c_num = models.IntegerField(default=1)  # 商品个数
    is_select = models.BooleanField(default=True)   # 是否选择商品

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):    # 订单
    user = models.ForeignKey(UserModel)  # 关联的用户
    o_num = models.CharField(max_length=64)  # 订单号
    # 0 代表已下单，未付款， 1已付款未发货， 2已付款已发货
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'axf_order'


class OrderGoodsModel(models.Model):
    goods = models.ForeignKey(Goods)  # 关联的商品
    order = models.ForeignKey(OrderModel)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'axf_order_goods'


