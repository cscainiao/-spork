import os

from flask import Blueprint, render_template, redirect, url_for, session, jsonify, request

from App.models import Area, Facility, House, db, HouseImage, Order
from utils import status_code
from utils.middleware import is_login
from utils.setting import UPLOAD_DIR

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/my_house/', methods=['GET'])
@is_login
def my_house():
    """
    渲染my_house页面
    """
    return render_template('my_house.html')


@house_blueprint.route('/show_my_house/', methods=['GET'])
@is_login
def show_my_house():
    """
    渲染发布的房源信息
    """
    user_id = session['user_id']
    houses = House.query.filter(House.user_id == user_id).all()
    house_info = [house.to_dict() for house in houses]
    return jsonify(code=status_code.OK, house_info=house_info)


@house_blueprint.route('/new_house/', methods=['GET'])
@is_login
def new_house():
    """
    渲染mewhouse页面
    """
    return render_template('newhouse.html')


@house_blueprint.route('/new_house_show/', methods=['GET'])
@is_login
def new_house_show():
    """
    展示区域和配套设施
    """
    areas = Area.query.all()
    facilitys = Facility.query.all()
    return jsonify(area=[area.to_dict() for area in areas],
                   facility=[facility.to_dict() for facility in facilitys])


@house_blueprint.route('/publish_house/', methods=['POST'])
@is_login
def publish_house():
    """
    发布新房源
    """
    data = request.form.to_dict()
    user_id = session['user_id']
    facility_ids = request.form.getlist('facility')

    house = House()
    house.user_id = user_id
    house.title = data.get('title')
    house.price = data.get('price')
    house.area_id = data.get('area_id')
    house.address = data.get('address')
    house.room_count = data.get('room_count')
    house.acreage = data.get('acreage')
    house.unit = data.get('unit')
    house.capacity = data.get('capacity')
    house.beds = data.get('beds')
    house.deposit = data.get('deposit')
    house.min_days = data.get('min_days')
    house.max_days = data.get('max_days')

    facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
    house.facilities = facility_list

    house.add_update()

    return jsonify(code=status_code.OK, house_id=house.id)


@house_blueprint.route('/add_house_img/', methods=['POST'])
@is_login
def add_house_img():
    """
    添加房屋图片
    """
    house_id = request.form.get('house_id')
    house_img = request.files.get('house_image')
    house_img_url = os.path.join(UPLOAD_DIR, house_img.filename)
    house_img.save(house_img_url)
    show_url = os.path.join('/static/upload', house_img.filename)

    house_image = HouseImage()
    house_image.house_id = house_id
    house_image.url = show_url
    house_image.add_update()
    house_imgs = HouseImage.query.filter(HouseImage.house_id == house_id).all()
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = show_url
        house.add_update()

    return jsonify(house_imgs=[houseimg.to_dict() for houseimg in house_imgs], code=status_code.OK)


@house_blueprint.route('/house_detail/')
@is_login
def house_detail():
    """
    跳转房屋详情页面
    """
    return render_template('detail.html')


@house_blueprint.route('/house_details/<int:id>/', methods=['GET'])
@is_login
def house_details(id):
    """
    刷新房屋信息
    """
    house = House.query.get(id)
    house_info = house.to_full_dict()
    return jsonify(code=status_code.OK, house_info=house_info)


@house_blueprint.route('/search/', methods=['GET'])
def search():
    """
    跳转搜索页面
    """
    return render_template('search.html')


@house_blueprint.route('/house_search/', methods=['GET'])
def house_search():
    area_id = request.args.get('aid')
    sd = request.args.get('sd')
    ed = request.args.get('ed')
    # 先过滤自己房屋不显示
    if 'user_id' in session:
        houses = House.query.filter(House.user_id != session['user_id'])
    else:
        houses = House.query.all()

    # 过滤地区
    houses_area = houses.filter_by(area_id=area_id)
    # 过滤已经下单的房屋时间段
    orders1 = Order.query.filter(Order.begin_date >= sd, Order.begin_date <= ed)
    orders2 = Order.query.filter(Order.end_date >= sd, Order.end_date <= ed)
    orders3 = Order.query.filter(Order.begin_date >= sd, Order.end_date <= sd)
    orders4 = Order.query.filter(Order.end_date <= sd, Order.end_date >= ed)
    house_ids1 = [order.house_id for order in orders1]
    house_ids2 = [order.house_id for order in orders2]
    house_ids3 = [order.house_id for order in orders3]
    house_ids4 = [order.house_id for order in orders4]

    house_ids = list(set(house_ids1 + house_ids2 + house_ids3 + house_ids4))
    search_houses = houses_area.filter(House.id.notin_(house_ids))
    search_houses_info = [house.to_dict() for house in search_houses]
    return jsonify(code=status_code.OK, search_houses_info=search_houses_info)