

OK = 200
SUCCESS = {'code': '200', 'msg': '请求成功'}
DB_ERROR = {'code': '201', 'msg': '数据库出问题'}

# 用户模块
USER_REGISTER_DATA_NOT_NULL = {'code': '1001', 'msg': '请填写完整参数'}
USER_REGISTER_MOBILE_ERROR = {'code': '1002', 'msg': '手机号码不正确'}
USER_REGISTER_PASSWORD_ERROR = {'code': '1003', 'msg': '请确认两次密码一致'}
USER_REGISTER_MOBILE_EXIST = {'code': '1004', 'msg': '手机号已注册,请直接登录'}

USER_LOGIN_MOBILE_NOT_EXIST = {'code': '1005', 'msg': '手机号未注册'}
USER_LOGIN_PASSWORD_ERROR = {'code': '1006', 'msg': '账号或者密码错误'}

PROFILE_IMAGE_ERROR = {'code': '1007', 'msg': '图片格式错误'}
PROFILE_IMAGE_IS_NOT_VALID = {'code': '1008', 'msg': '用户名已存在'}

AUTH_NOT_ALL_NAME_ID_CARD = {'code': '1009', 'msg': '请填写真实姓名和身份证'}
AUTH_ID_CARD_IS_NOT_VALID = {'code': '1010', 'msg': '请填写正确的身份证号码'}