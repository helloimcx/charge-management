from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.sign_in, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.sign_in, name='login'),
    url(r'^logout$', views.logout, name='logout'),

]