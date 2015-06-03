# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matan', '0002_categories_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='term',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='theorem',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='author',
            name='date_pub',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categories',
            name='date_pub',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='term',
            name='date_pub',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='theorem',
            name='date_pub',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
