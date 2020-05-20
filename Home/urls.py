from django.conf.urls import url,include
from . import views

urlpatterns = [
     url(r'^$', views.homepage, name='homepage'),
     url(r'contact/$', views.contact, name='contact'),
     url(r'index_worker/$', views.homepage_worker, name='homepage_worker'),

]
