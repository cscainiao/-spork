import datetime

from flask import Blueprint, render_template, session, request, jsonify

from App.models import House, Order
from utils import status_code
from utils.middleware import is_login

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/book_house/', methods=['GET'])
@is_login
def book_house():
    """
    跳转预定页面
    """
    return render_template('booking.html')


@order_blueprint.route('/orders/', methods=['GET'])
@is_login
def orders():
    """
    跳转下单页面
    """
    return render_template('orders.html')


@order_blueprint.route('/get_order/<int:id>/', methods=['POST'])
@is_login
def get_order(id):
    """
    提交我的订单
    """
    user_id = session['user_id']
    begin_date = datetime.datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
    end_date = datetime.datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
    times = end_date - begin_date
    days = times.days + 1
    house = House.query.get(id)
    price = house.price
    amount = days * price
    order = Order()
    order.user_id = user_id
    order.house_id = id
    order.begin_date = begin_date
    order.end_date = end_date
    order.days = days
    order.house_price = price
    order.amount = amount
    order.add_update()

    return jsonify(code=status_code.OK)


@order_blueprint.route('/my_orders/', methods=['GET'])
@is_login
def my_orders():
    """
    跳转我的订单页面
    """
    return render_template('orders.html')


@order_blueprint.route('/show_my_orders/', methods=['GET'])
@is_login
def show_my_orders():
    """
    展示我的订单详情
    """
    my_orders = Order.query.filter(Order.user_id == session['user_id'])
    orders_info = [my_order.to_dict() for my_order in my_orders]
    return jsonify(code=status_code.OK, orders_info=orders_info)


@order_blueprint.route('/custom_orders/', methods=['GET'])
@is_login
def custom_orders():
    """
    跳转客户订单页面
    """
    return render_template('custom_orders.html')


@order_blueprint.route('/show_custom_orders/', methods=['GET'])
@is_login
def show_custom_orders():
    """
    展示客户订单详情
    """
    user_id = session['user_id']
    houses = House.query.filter(House.user_id == user_id)
    houses_ids = [house.id for house in houses]
    custom_orders = Order.query.filter(Order.house_id.in_(houses_ids)).all()
    custom_orders_info = [custom_order.to_dict() for custom_order in custom_orders]
    return jsonify(code=status_code.OK, custom_orders_info=custom_orders_info)


@order_blueprint.route('/accept_order/', methods=['PATCH'])
@is_login
def accept_order():
    order_id = request.form.get('order_id')

    order = Order.query.get(order_id)
    order.status = 'WAIT_PAYMENT'
    order.add_update()
    return jsonify(code=200)


@order_blueprint.route('/refuse_order/', methods=['PATCH'])
@is_login
def refuse_order():
    order_id = request.form.get('order_id')

    reject_reason = request.form.get('reject_reason')
    order = Order.query.get(order_id)
    order.status = 'REJECTED'
    order.comment = reject_reason
    order.add_update()
    return jsonify(code=200)