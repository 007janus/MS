# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0004_auto_20151224_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vip', models.IPAddressField(verbose_name='VIP')),
                ('ip', models.IPAddressField(verbose_name='IP')),
                ('outip', models.IPAddressField(verbose_name='\u5916\u7f51IP')),
                ('farip', models.IPAddressField(verbose_name='\u8fdc\u7a0b\u7ba1\u7406IP')),
                ('desc', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': 'IP\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MysqlAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(verbose_name='IP')),
                ('sql', models.CharField(max_length=50, verbose_name='\u6570\u636e\u5e93')),
                ('sqlaccount', models.CharField(max_length=50, verbose_name='\u5e10\u53f7')),
                ('pas', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('authority', models.CharField(max_length=50, verbose_name='\u6743\u9650')),
                ('ran', models.CharField(max_length=50, verbose_name='\u8bbf\u95ee\u8303\u56f4')),
                ('desc', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u6570\u636e\u5e93\u5e10\u53f7\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u5b57')),
                ('ip', models.IPAddressField(verbose_name='\u8bbf\u95ee\u8303\u56f4')),
                ('url', models.CharField(max_length=50, verbose_name='\u5730\u5740')),
                ('account', models.CharField(max_length=50, verbose_name='\u5e10\u53f7')),
                ('authority', models.CharField(max_length=50, verbose_name='\u6743\u9650')),
                ('pas', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('desc', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u5176\u4ed6\u5e10\u53f7\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(verbose_name='IP')),
                ('osaccount', models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u5e10\u53f7')),
                ('pas', models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u5bc6\u7801')),
                ('farip', models.CharField(max_length=50, verbose_name='\u8fdc\u7a0b\u7ba1\u7406\u5361IP')),
                ('faraccount', models.CharField(max_length=50, verbose_name='\u7ba1\u7406\u5361\u5e10\u53f7')),
                ('farpas', models.CharField(max_length=50, verbose_name='\u7ba1\u7406\u5361\u5bc6\u7801')),
                ('desc', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5e10\u53f7\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
    ]
