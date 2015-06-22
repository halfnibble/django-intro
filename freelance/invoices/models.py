from decimal import Decimal
from django.db import models
from clients.models import Client


class Invoice(models.Model):
    # Invoice terms options
    TERMS = (
        (15, 'NET15'),
        (30, 'NET30'),
        (60, 'NET60'),
    )
    # Status options
    STATUS = (
        ('PEND', 'Pending'),
        ('INV' , 'Invoiced'),
        ('PAID', 'Paid'),
    )

    client = models.ForeignKey(Client)
    invoiced_date = models.DateField('Invoiced On', null=True, blank=True)
    terms = models.IntegerField('Terms', choices=TERMS, default=15)
    status = models.CharField('Status', max_length=4, choices=STATUS,
        default='PEND')

    @property
    def total(self):
        print 'eh?'
        total = Decimal('0.00')

        for item in self.lineitem_set.all():
            print "item cost:", item.cost
            total += item.cost

        return total
    

    def __str__(self):
        return "Invoice #{0}. {1}.".format(self.id, self.get_status_display())

