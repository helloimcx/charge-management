from django.conf.urls import url
from .views import client_view

urlpatterns = [
    url(r'^$', client_view, name='client_view'),
]
