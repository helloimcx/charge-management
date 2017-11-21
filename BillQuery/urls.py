from django.conf.urls import url
from . import views
from . import assist

urlpatterns = [
    url(r'^customer$', views.customer, name='customer'),
    url(r'^datatable/', assist.pager_query, name='datatable')
]
