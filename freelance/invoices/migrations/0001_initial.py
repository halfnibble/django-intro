# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoiced_date', models.DateField(verbose_name=b'Invoiced On', blank=True)),
                ('terms', models.IntegerField(default=15, verbose_name=b'Terms', choices=[(15, b'NET15'), (30, b'NET30'), (60, b'NET60')])),
                ('status', models.CharField(default=b'PEND', max_length=4, verbose_name=b'Status', choices=[(b'PEND', b'Pending'), (b'INV', b'Invoiced'), (b'PAID', b'Paid')])),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
        ),
    ]
