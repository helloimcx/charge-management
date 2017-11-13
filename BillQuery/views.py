from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Authentication.decorators import required_login
from Authentication.models import Phone
from Authentication import assist
from .models import Bill

import logging

logger = logging.getLogger('django')


# 可以修改 page.html 的 grid_data, colNames, colModel
# 模板来自 git@github.com:bopoda/ace.git
@required_login
def stub(request):
    context = {
        'phone_collection': Phone.objects.all()
    }
    return render(request, 'BillQuery/page.html', context)


# ['ID', 'Item', /*'Time',*/ 'Amount', 'Pay', 'Receive', 'Status'],
@required_login
def client_view(request):
    phone_number = request.session[assist.PHONE]
    bills = Bill.objects.filter(phone__phone=phone_number).select_related('item')
    context = {
        'phone_number':phone_number,
        'bill_list':bills
    }
    return render(request, 'BillQuery/page.html', context)
