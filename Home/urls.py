from django.conf.urls import url,include
from . import views

urlpatterns = [
     url(r'^index/$', views.homepage, name='homepage'),
     url(r'^contact/$', views.contact, name='contact'),
]
