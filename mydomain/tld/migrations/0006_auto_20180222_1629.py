# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tld', '0005_auto_20180222_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheapest',
            name='popularity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cheapest',
            name='reg_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='cheapest',
            name='reg_registrar',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='cheapest',
            name='renew_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='cheapest',
            name='renew_registrar',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='cheapest',
            name='tran_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='cheapest',
            name='tran_registrar',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='domain',
            name='cate',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='popular',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='registry',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='domain',
            name='restrictions',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='domain',
            name='sources',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='status',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='register',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='renewal',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='transfer',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='whois',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='registrar',
            name='rating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='registrar',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
