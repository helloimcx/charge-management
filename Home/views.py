from Authentication.decorators import required_login
from django.shortcuts import render
from django.contrib import messages
from Authentication.assist import PHONE, is_login
from Authentication.models import Phone
from .models import Suggestions


def homepage(request):
    if is_login(request):
        phone_account = Phone.objects.get(phone=request.session[PHONE])
        context = {
            "phone_account": phone_account
        }
        return render(request, 'Home/index.html', context)
    else:
        return render(request, 'Home/index.html')


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
        messages.add_message(request, messages.SUCCESS, "发送成功！感谢您的建议，我们会尽快回复！")
        return render(request, 'Home/contact.html', context)
    else:
        return render(request, 'Home/contact.html', context)

