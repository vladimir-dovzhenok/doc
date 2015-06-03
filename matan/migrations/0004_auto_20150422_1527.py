# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matan', '0003_auto_20150422_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_pub',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categories',
            name='date_pub',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='term',
            name='date_pub',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='theorem',
            name='date_pub',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
    ]
