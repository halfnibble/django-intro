from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.InvoiceList.as_view(), name='invoices'),
    url(r'^(?P<pk>\d+)/$', views.InvoiceDetail.as_view(),
        name='invoice_detail'),
    url(r'^create/$', views.CreateInvoice.as_view(), name='create_invoice'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateInvoice.as_view(),
        name='update_invoice'),
    url(r'^send/(?P<pk>\d+)/$', views.SendInvoice.as_view(),
        name='send_invoice'),
]