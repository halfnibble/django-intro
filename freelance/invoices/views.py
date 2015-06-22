from django.shortcuts import render
from django.views import generic

from .models import Invoice


class InvoiceList(generic.ListView):
    model = Invoice
    context_object_name = 'invoices'


class InvoiceDetail(generic.DetailView):
    model = Invoice
    context_object_name = 'invoice'

