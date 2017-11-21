from django.shortcuts import render


# Create your views here.
from Authentication.decorators import required_login
from Authentication.models import Phone
from Authentication.assist import PHONE
from .models import Bill


@required_login
def customer(request):
    phone_account = Phone.objects.get(phone=request.session[PHONE])
    bill_collection = Bill.objects.filter(phone__phone=phone_account)
    context = {
        "phone_account": phone_account,
        "bill_collection": bill_collection
    }
    return render(request, 'BillQuery/customer.html', context)


def workder(request):
    pass

