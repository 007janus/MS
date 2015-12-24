# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0003_auto_20151223_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vip', models.IPAddressField(verbose_name='VIP')),
                ('ip', models.IPAddressField(verbose_name='IP')),
                ('outip', models.IPAddressField(verbose_name='\u5916\u7f51IP')),
                ('service', models.CharField(max_length=50, verbose_name='\u670d\u52a1')),
                ('rd', models.CharField(max_length=50, verbose_name='RD\u63a5\u53e3\u4eba')),
                ('desc', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host',
            name='Uid',
            field=models.CharField(default=b'null', max_length=50, verbose_name='U\u4f4d'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='Unum',
            field=models.CharField(default=b'null', max_length=50, verbose_name='U\u6570'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='cpu',
            field=models.CharField(default=b'null', max_length=50, verbose_name='CPU\u578b\u53f7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='disksize',
            field=models.CharField(default=b'null', max_length=50, verbose_name='\u78c1\u76d8\u5927\u5c0f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='house',
            field=models.CharField(default=b'null', max_length=50, verbose_name='\u673a\u623f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='houseid',
            field=models.CharField(default=b'null', max_length=50, verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='memorysize',
            field=models.CharField(default=b'null', max_length=50, verbose_name='\u5185\u5b58\u5927\u5c0f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='Manufacturer',
            field=models.CharField(max_length=50, verbose_name='\u5236\u9020\u5546'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu_core',
            field=models.CharField(max_length=50, verbose_name='CPU\u6838\u6570'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='desc',
            field=models.CharField(default=b'null', max_length=50, verbose_name='\u5907\u6ce8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.CharField(max_length=50, verbose_name='\u78c1\u76d8\u578b\u53f7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='ip',
            field=models.IPAddressField(verbose_name='IP'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='memory',
            field=models.CharField(max_length=50, verbose_name='\u5185\u5b58\u578b\u53f7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='model_name',
            field=models.CharField(max_length=50, verbose_name='\u578b\u53f7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='osversion',
            field=models.CharField(max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='product',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x9e\x8b\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='vendor_id',
            field=models.CharField(max_length=50, verbose_name='\u4f9b\u5e94\u5546ID'),
            preserve_default=True,
        ),
    ]
