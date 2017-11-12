from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import  json
from django.http import HttpResponseRedirect
from Authentication.assist import is_login
from Authentication.models import Phone
from Authentication.decorators import required_login
from django.contrib import messages
import traceback
from django.http import request

# Create your views here.


def getPhone(phone):
    try:
        phone_account=Phone.objects.get(phone=phone);
        return phone_account;
    except:

        return None
def payment(request):

    return render(request,"Payment/Payment.html")




def form(request):

    return render(request,"Payment/form.html")




#确认账单
@csrf_exempt
def confirmpay(request):

    return  render(request,"Payment/form.html")





#验证充值的有效性 异步ajax
@csrf_exempt
def pay(request):
    if request.method == 'POST':
     phone = request.POST.get('phone', False)
     phone_account=getPhone(phone)

     if phone_account is not None:
        return_json = {'result': 1}
        return HttpResponse(json.dumps(return_json), content_type='application/json')

     else:
         return_json = {'result': 0}
         return HttpResponse(json.dumps(return_json), content_type='application/json')


def test(request):
    channel = request.POST.get('channel', False)
    way = request.POST.get('way', False)
    phone = request.POST.get('phone', False)
    money = request.POST.get('money', False)
    phone_account=Phone.objects.get(phone=phone)
    


    return render(request,'Payment/test.html')

