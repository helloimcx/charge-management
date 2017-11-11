from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Authentication.decorators import required_login


# 暂时没有帐单数据，只能使用账户数据
@required_login
def stub(request):
    return render(request, 'BillQuery/page.html')
