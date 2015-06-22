from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invoice, InvoiceAdmin)