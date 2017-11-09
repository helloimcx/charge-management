# coding: utf-8
from .models import Phone
from .utils.exceptions import LogInWithoutAuthentication

PHONE = 'auth_phone'


def authenticate(phone, password):
    """
    验证函数
    :param phone: 用户的phone
    :param password: 用户的password
    :return: 用户不存在或其他异常返回(None，错误信息),用户存在且密码正确(user对象，True)， 密码错误则为(user对象， False)
    """

    if phone is not None:
        try:
            phone_account = Phone.objects.get(phone=phone)
            if phone_account.check_user_password(password):
                phone_account.auth = True
                return phone_account, True
            else:
                return phone_account, False
        except Phone.DoesNotExist:
            return None, 'DoesNotExist'
        except Exception as e:
            return None, str(e)


def login(request, phone_account):
    if not hasattr(phone_account, 'auth'):
        raise LogInWithoutAuthentication

    if PHONE in request.session:
        request.session.flush()
    else:
        request.session.cycle_key()

    request.session[PHONE] = phone_account.phone
    phone_account.save()
    request.user = phone_account


def logout(request):
    request.session.flush()


def is_login(request):
    return PHONE in request.session
