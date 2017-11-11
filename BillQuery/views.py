from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Authentication.decorators import required_login
from Authentication.models import Phone


# 暂时没有帐单数据，只能使用账户数据；通过 127.0.0.1:8000/bill 访问
# 模板来自 git@github.com:bopoda/ace.git
@required_login
def stub(request):
    context = {
        "phone_collection": Phone.objects.all()
    }
    return render(request, 'BillQuery/page.html', context)
