from flask import session, redirect, url_for

from functools import wraps


def is_login(func):
    """
    装饰器:用于登录验证
    """
    @wraps(func)
    def check_login(*args, **kwargs):
        user_session = session.get('user_id')
        if user_session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login_get'))

    return check_login
