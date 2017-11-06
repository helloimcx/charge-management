from django.http import HttpResponseRedirect
import traceback
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib import messages
from .models import Phone
from django.contrib import auth
from .assist import authenticate,login,is_login


def register(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', False)
        pwd = request.POST.get('password', False)
        pwd_confirm = request.POST.get('password_confirm', False)
        if pwd != pwd_confirm:
            messages.add_message(request, messages.ERROR, "两次输入密码不一致！")
            return render(request, 'Authentication/signup.html')
        if phone is not False and pwd is not False:
            try:
                Phone.create_phone(phone=phone, password=pwd)
            except IntegrityError:
                messages.add_message(request, messages.ERROR, "该手机号已注册！")
                return render(request, 'Authentication/signup.html')
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请求出错！")
                return render(request, 'Authentication/signup.html')
            else:
                context = {
                    "phone_number": phone
                }
                messages.add_message(request, messages.SUCCESS, "注册成功！")
                return render(request, 'Authentication/login.html', context)
        else:
            messages.add_message(request, messages.ERROR, "请求出错！")
            return render(request, 'Authentication/signup.html')
    else:
        return render(request, 'Authentication/signup.html')


def sign_in(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', False)
        pwd = request.POST.get('password', False)
        phone_account, status = authenticate(phone, pwd)
        try:
            if phone_account is not None:
                if status is False:
                    messages.add_message(request, messages.ERROR, "密码错误！")
                    return render(request, 'Authentication/login.html')
                if phone_account.is_active:
                    login(request, phone_account)
                    next_url = request.GET.get('next', '/home/index')
                    return HttpResponseRedirect(next_url)
                else:
                    messages.add_message(request, messages.ERROR, "该手机已停机！")
                    return render(request, 'Authentication/login.html')
            else:
                messages.add_message(request, messages.ERROR, "当前账号不存在！")
                return render(request, 'Authentication/login.html')
        except:
            print(traceback.format_exc())
    else:
         if is_login(request):
            return HttpResponseRedirect('/home/index')
         request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
         return render(request, 'Authentication/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/home/index")


