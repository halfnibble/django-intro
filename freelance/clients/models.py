from django.db import models


class Client(models.Model):
    company = models.CharField('Company', max_length=100)
    contact = models.CharField('Contact', max_length=100, blank=True)
    email = models.EmailField('Contact Email')

    def __str__(self):
        return self.company
