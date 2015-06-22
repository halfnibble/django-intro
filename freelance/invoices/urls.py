from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.InvoiceList.as_view(), name='invoices'),
    url(r'^(?P<pk>\d+)/$', views.InvoiceDetail.as_view(),
        name='invoice_detail'),
]