# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='text',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
            preserve_default=True,
        ),
    ]
