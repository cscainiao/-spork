import random


def total_money(user):
    user_carts = user.cartmodel_set.all()
    totalMoney = 0
    for user_cart in user_carts:
        if user_cart.is_select == True:
            price = user_cart.goods.price
            num = user_cart.c_num
            money = price * num
            totalMoney += money
    return totalMoney


def get_order_random_id():
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    order = ''
    for i in range(28):
        order += random.choice(s)
    return order

