# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='name',
            field=models.CharField(max_length=240, verbose_name=b'Item Name'),
        ),
    ]
