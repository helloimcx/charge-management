
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Home.views import page
from .utils.functions import error_json, success_json
from .forms import RegisterForm
import traceback
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from .models import Phone
from . import models,assist
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .assist import authenticate,login,is_login
#from django.contrib.auth import login


def index(request):
    return HttpResponse("Hello, world. You're at the authentication index.")



def register(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', False)
        pwd = request.POST.get('password',False)

        if phone is not False and pwd is not False:
            try:
                Phone.create_phone(phone=phone, password=pwd)

            except IntegrityError as ige:
                return JsonResponse(error_json(msg="Phone already exists", url=None))
            except Exception as e:
                return JsonResponse(error_json(msg="something wrong", url=None, traceback=traceback.format_exc()))
            else:
                return render(request, 'Authentication/login.html')
        else:
            return JsonResponse(error_json(msg='Bad information', url=None))
    else:
        return render(request, 'Authentication/signup.html')


def sign_in(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', False)
        pwd = request.POST.get('password', False)
        phone_account,status=authenticate(phone,pwd)

        try:
            if phone_account is not None:
                if status is False:
                    return JsonResponse(error_json(msg="Wrong password", url=''))
                if phone_account.is_active:
                    login(request, phone_account)
                    next_url = request.GET.get('next','/home/index')
                    return HttpResponseRedirect(next_url)

                else:
                    return JsonResponse(error_json(msg="This phoneaccount is deactivated", url=None))
            else:
                return JsonResponse(error_json(msg=status, url=None))
        except:
            print(traceback.format_exc())

    else:
         if is_login(request):
            return HttpResponseRedirect('/home/index')
         request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
         return render(request,'Authentication/login.html')
#

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/home/index")


