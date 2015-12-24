# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0002_auto_20151223_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='desc',
            field=models.CharField(default=b'woqu', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u540d'),
            preserve_default=True,
        ),
    ]
