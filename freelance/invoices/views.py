from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Invoice


class InvoiceList(generic.ListView):
    model = Invoice
    context_object_name = 'invoices'


class InvoiceDetail(generic.DetailView):
    model = Invoice
    context_object_name = 'invoice'


class SendInvoice(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'invoice_detail'

    def send_invoice(self, invoice):
        msg = ('Please review the following invoice:\n' +
               'Invoice #{0}: {1}\n\n' + 
               'Invoiced on {2}.').format(
                    invoice.id,
                    self.request.build_absolute_uri(
                        reverse('invoice_detail', kwargs={'pk': invoice.id})
                    ),                    
                    invoice.invoiced_date
                )

        send_mail(
            subject='Invoice #{0}'.format(invoice.id),
            message=msg,
            from_email='no-reply@localhost',
            recipient_list=[invoice.client.email],
            fail_silently=False
        )

    def get_redirect_url(self, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=kwargs['pk'])

        if invoice.status == 'PEND':
            invoice.status = 'INV'
        if invoice.invoiced_date is None:
            invoice.invoiced_date = datetime.now()
        invoice.save()

        self.send_invoice(invoice=invoice)

        messages.info(self.request,
            "Invoice #{0} sent to client.".format(invoice.id)
        )

        return super(SendInvoice, self).get_redirect_url(*args, **kwargs)


