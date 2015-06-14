# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matan', '0004_auto_20150422_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='section')),
                ('section', models.ForeignKey(blank=True, to='matan.Chapter', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('editor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('text_chapter', models.ForeignKey(verbose_name='Chapter', to='matan.Chapter')),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={},
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_pub',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='date_pub',
        ),
        migrations.RemoveField(
            model_name='term',
            name='date_pub',
        ),
        migrations.RemoveField(
            model_name='theorem',
            name='date_pub',
        ),
        migrations.AlterField(
            model_name='categories',
            name='term',
            field=models.ManyToManyField(to='matan.Term', verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='theorem',
            field=models.ManyToManyField(to='matan.Theorem', verbose_name='\u0422\u0435\u043e\u0440\u0435\u043c\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='theorem',
            name='term',
            field=models.ManyToManyField(to='matan.Term', verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='text_body',
            field=models.ManyToManyField(related_name='authors', to='matan.TextSection', blank=True),
        ),
        migrations.AddField(
            model_name='term',
            name='text_body',
            field=models.ManyToManyField(related_name='therms', to='matan.TextSection', blank=True),
        ),
        migrations.AddField(
            model_name='theorem',
            name='text_body',
            field=models.ManyToManyField(related_name='theorems', to='matan.TextSection', blank=True),
        ),
    ]
