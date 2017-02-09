# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-09 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('value', models.DecimalField(decimal_places=6, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='RateSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('base_currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djmoney_rates.RateSource'),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('source', 'currency')]),
        ),
    ]
