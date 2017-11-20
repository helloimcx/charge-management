# coding: utf-8

from django.shortcuts import redirect
from django.conf import settings
import functools
from .assist import PHONE, is_login
from .models import Phone


def user_pass_decorator(redirect_field_name='next', redirect_url=None):

    def decorator(func):
        @functools.wraps(func)
        def wrap(request, *args, **kwargs):
            if is_login(request):
                phone_account = Phone.objects.get(phone=request.session[PHONE])
                request.user = phone_account
                return func(request, *args, **kwargs)
            else:
                if redirect_url is None:
                    return redirect('%s?%s=%s' %(settings.LOGIN_URL, redirect_field_name, request.path))
                else:
                    return redirect('%s?%s=%s' %(redirect_url, redirect_field_name, request.path))

        return wrap
    return decorator


def required_login(function=None, redirect_field_name='next', redirect_url=None):

    actual_decorator = user_pass_decorator(
        redirect_field_name= redirect_field_name,
        redirect_url= redirect_url
    )

    if function:
        actual_decorator = actual_decorator(function)
    return actual_decorator

