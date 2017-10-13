
from django.shortcuts import render
from Authentication.decorators import required_login
from django.contrib import auth
from django.http import HttpResponseRedirect
import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join
from Authentication.assist import PHONE, is_login
from Authentication.models import Phone
from .models import Suggestions

def get_page_or_404(name):
    try:
        file_path=safe_join(settings.SITE_PAGES_DIRECTORY,name)
    except ValueError:
        raise Http404('PAGE NOT FOUND')
    else:
        if not os.path.exists(file_path):
            raise Http404('PAGE NOT FOUND')

    with open(file_path,'r') as f:
        page=Template(f.read())

    return page


def page(request,slug='index'):
    if is_login(request):
        phone_account = Phone.objects.get(phone=request.session[PHONE])
        request.user = phone_account
    file_name='{}.html'.format(slug)
    page=get_page_or_404(file_name)
    context={
        'slug':slug,
        'page':page,
    }
    return render(request,'Home/page.html',context)

@required_login
def contact(request):
    if request.method=='POST':
        user = Phone.objects.get(phone=request.session[PHONE])
        phone=user.phone
        title=request.POST.get('title',None)
        content=request.POST.get('messages',None)
        Suggestions.objects.create(phone=phone,title=title,content=content)
        return HttpResponseRedirect('/home/index')

    else:
        return render(request,'Home/contact.html')

