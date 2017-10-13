from django.conf.urls import url,include
from . import views

urlpatterns = [

     url(r'^page/(?P<slug>[\w./-]+)/$',views.page,name='page'),
     url(r'^index/$',views.page,name='homepage'),
     url(r'^contact/$',views.contact,name='contact'),

]
