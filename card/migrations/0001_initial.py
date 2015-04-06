# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_id', models.CharField(unique=True, max_length=16, verbose_name=b'Card id', blank=True)),
                ('pin', models.IntegerField(verbose_name=b'Pin code', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Card status')),
                ('balance', models.DecimalField(default=Decimal('0'), max_digits=8, decimal_places=2)),
            ],
            options={
                'db_table': 'card',
                'verbose_name': 'Card',
            },
        ),
        migrations.CreateModel(
            name='CardOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_operation', models.IntegerField(verbose_name=b'Pin code', blank=True)),
                ('operation_time', models.DateTimeField(auto_now=True, verbose_name=b'Operation time')),
                ('amount', models.DecimalField(default=Decimal('0'), verbose_name=b'Amount', max_digits=8, decimal_places=2)),
                ('card', models.ForeignKey(to='card.Card')),
            ],
            options={
                'db_table': 'card_operations',
                'verbose_name': 'Card operations',
            },
        ),
    ]
