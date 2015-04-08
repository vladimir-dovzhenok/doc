# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('biagrafiya', models.TextField(verbose_name='\u0411\u0438\u0430\u0433\u0440\u0430\u0444\u0438\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d')),
                ('determination', models.TextField(verbose_name='\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theorem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u0422\u0435\u043e\u0440\u0435\u043c\u0430')),
                ('substantiation', models.TextField(verbose_name='\u0414\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e')),
                ('author', models.ManyToManyField(to='matan.Author', verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('term', models.ManyToManyField(to='matan.Term', verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categories',
            name='term',
            field=models.ManyToManyField(to='matan.Term', verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categories',
            name='theorem',
            field=models.ManyToManyField(to='matan.Theorem', verbose_name='\u0422\u0435\u043e\u0440\u0435\u043c\u0430'),
            preserve_default=True,
        ),
    ]
