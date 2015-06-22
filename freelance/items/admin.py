from django.contrib import admin
from .models import LineItem

class LineItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(LineItem, LineItemAdmin)