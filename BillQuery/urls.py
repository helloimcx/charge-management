from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^customer$', customer, name='customer'),
]
