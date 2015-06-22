# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20150622_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240, verbose_name=b'Item Name', blank=True)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('quantity', models.DecimalField(verbose_name=b'Quantity', max_digits=5, decimal_places=2)),
                ('rate', models.DecimalField(verbose_name=b'Rate', max_digits=6, decimal_places=2)),
                ('invoice', models.ForeignKey(to='invoices.Invoice')),
            ],
        ),
    ]
