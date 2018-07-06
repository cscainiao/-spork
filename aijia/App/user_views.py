import os
import re

from flask import Blueprint, request, render_template, session, redirect, url_for
from flask.json import jsonify

from App.models import db, User
from utils import status_code
from utils.middleware import is_login
from utils.setting import UPLOAD_DIR

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/register/', methods=['GET'])
def register_get():
    if request.method == 'GET':
        return render_template('register.html')


@user_blueprint.route('/register/', methods=['POST'])
def register_post():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not all([mobile, password1, password2]):
            return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
        if not re.match(r'^1[34578]\d{9}$', mobile):
            return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)
        if password1 != password2:
            return jsonify(status_code.USER_REGISTER_PASSWORD_ERROR)
        user = User.query.filter_by(phone=mobile).first()
        if user:
            return jsonify(status_code.USER_REGISTER_MOBILE_EXIST)
        else:
            user = User()
            user.phone = mobile
            user.password = password1
            user.add_update()
            return jsonify(status_code.SUCCESS)


@user_blueprint.route('/login/', methods=['GET'])
def login_get():
    if request.method == 'GET':
        return render_template('login.html')


@user_blueprint.route('/logout/', methods=['GET'])
def logout():
    """
    注销
    :return:
    """
    session.clear()
    return redirect(url_for('user.login_get'))


@user_blueprint.route('/login/', methods=['POST'])
def login_post():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        user = User.query.filter_by(phone=mobile).first()
        if user:
            if not user.check_pwd(password):
                return jsonify(status_code.USER_LOGIN_PASSWORD_ERROR)
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)

        else:
            return jsonify(status_code.USER_LOGIN_MOBILE_NOT_EXIST)


@user_blueprint.route('/my/', methods=['GET'])
@is_login
def my():
    """
    跳转个人中心
    """
    if request.method == 'GET':
        user = User.query.get(session['user_id'])
        return render_template('my.html', user=user)


@user_blueprint.route('/profile/', methods=['GET'])
@is_login
def profile_get():
    """
    跳转修改页面
    """
    if request.method == 'GET':
        return render_template('profile.html')


@user_blueprint.route('/profile/', methods=['PATCH'])
@is_login
def profile_patch():
    """
    图片上传
    """
    file = request.files.get('avatar')
    if not re.match(r'image/.*', file.mimetype):
        return jsonify(status_code.PROFILE_IMAGE_ERROR)
    # 保存
    image_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(image_path)

    user = User.query.get(session['user_id'])
    avatar_path = os.path.join('/static', os.path.join('upload', file.filename))
    user.avatar = avatar_path
    try:
        user.add_update()
    except:
        db.session.rollback()
        return jsonify(status_code.DB_ERROR)

    return jsonify(code=status_code.OK, image_url=avatar_path)


@user_blueprint.route('/update_name/', methods=['PATCH'])
@is_login
def update_name():
    """
    修改用户名
    """
    name = request.form.get('name')
    user = User.query.filter_by(name=name).first()
    if user:
        return jsonify(status_code.PROFILE_IMAGE_IS_NOT_VALID)
    else:
        user = User.query.get(session['user_id'])
        user.name = name
        try:
            user.add_update()
        except:
            db.session.rollback()
            return jsonify(status_code.DB_ERROR)

        return jsonify(code=status_code.OK, name=name)


@user_blueprint.route('/auth/', methods=['GET'])
@is_login
def auth():
    return render_template('auth.html')


@user_blueprint.route('/auth/', methods=['PATCH'])
@is_login
def user_auth():
    """
    实名认证
    :return:
    """
    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')

    if not all([real_name, id_card]):
        return jsonify(status_code.AUTH_NOT_ALL_NAME_ID_CARD)
    if not re.match(r'^[1-9]\d{17}$', id_card):
        return jsonify(status_code.AUTH_ID_CARD_IS_NOT_VALID)

    user = User.query.get(session['user_id'])
    user.id_name = real_name
    user.id_card = id_card
    try:
        user.add_update()
    except:
        return jsonify()

    return jsonify(status_code.SUCCESS)


@user_blueprint.route('/auth_show/', methods=['GET'])
@is_login
def auth_show():
    user = User.query.get(session['user_id'])
    return jsonify({'code': status_code.OK, 'user': user.to_auth_dict()})


@user_blueprint.route('/index/', methods=['GET'])
def index():

    return render_template('index.html')