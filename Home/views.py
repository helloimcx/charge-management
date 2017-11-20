from Authentication.decorators import required_login
from django.shortcuts import render
from django.contrib import messages
from Authentication.assist import *
from Authentication.models import Phone, Worker
from .models import Suggestions


def homepage(request):
    if is_login(request):
        phone_account = Phone.objects.get(phone=request.session[PHONE])
        customer = phone_account.customer
        context = {
            "customer": customer,
            "phone_account": phone_account
        }
        return render(request, 'Home/index_customer.html', context)
    else:
        return render(request, 'Home/index_customer.html')


def homepage_worker(request):
    if is_login_work(request):
        worker = Worker.objects.get(worker_id=request.session[WORKER])
        context = {
            "worker": worker,
        }
        return render(request, 'Home/index_worker.html', context)
    else:
        return render(request, 'Home/index_worker.html')


@required_login
def contact(request):
    phone_account = Phone.objects.get(phone=request.session[PHONE])
    context = {
        "phone_account": phone_account
    }
    if request.method == 'POST':
        phone = phone_account.phone
        title = request.POST.get('title', None)
        content = request.POST.get('messages', None)
        Suggestions.objects.create(phone=phone, title=title, content=content)
        messages.add_message(request, messages.SUCCESS, "发送成功！感谢您的建议，我们会尽快回复!")
        return render(request, 'Home/contact.html', context)
    else:
        return render(request, 'Home/contact.html', context)


def helloworld(request):
    return render(request, 'Home/helloworld.html')
