# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=100, verbose_name=b'Company')),
                ('contact', models.CharField(max_length=100, verbose_name=b'Contact', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Contact Email')),
            ],
        ),
    ]
