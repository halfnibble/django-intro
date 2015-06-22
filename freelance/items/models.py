from django.db import models
from invoices.models import Invoice


class LineItem(models.Model):
    invoice = models.ForeignKey(Invoice)
    name = models.CharField('Item Name', max_length=240)
    description = models.TextField('Description', blank=True)
    quantity = models.DecimalField('Quantity', max_digits=5, decimal_places=2)
    rate = models.DecimalField('Rate', max_digits=6, decimal_places=2)

    @property
    def cost(self):
        return self.quantity * self.rate

    def __str__(self):
        return "{0} - ${1:.2f}".format(self.name, self.cost)
    
