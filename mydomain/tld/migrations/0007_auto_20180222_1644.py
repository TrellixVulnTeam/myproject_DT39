# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tld', '0006_auto_20180222_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrar',
            old_name='key',
            new_name='keyword',
        ),
        migrations.AlterModelTable(
            name='domain',
            table='tld_domain',
        ),
        migrations.AlterModelTable(
            name='price',
            table='tld_price',
        ),
        migrations.AlterModelTable(
            name='registrar',
            table='tld_registrar',
        ),
    ]
