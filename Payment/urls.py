
from django.conf.urls import url,include
from . import views


urlpatterns = [
     url(r'^$', views.payment, name='payment'),
     url(r'^pay/$',views.pay,name='pay'),
     url(r'^form/$', views.confirmpay, name='form'),
     url(r'^test/$', views.test, name='test'),
]
