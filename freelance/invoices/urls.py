from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.InvoiceList.as_view(), name='invoices'),
    url(r'^(?P<pk>\d+)/$', views.InvoiceDetail.as_view(),
        name='invoice_detail'),
    url(r'^send/(?P<pk>\d+)/$', views.SendInvoice.as_view(),
        name='send_invoice'),
]