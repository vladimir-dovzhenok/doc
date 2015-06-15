# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('text', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='section')),
                ('section', models.ForeignKey(blank=True, to='matan.Chapter', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextBodyMixin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('editor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('text_chapter', models.ForeignKey(related_name='text_sections', verbose_name='Chapter', to='matan.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='TextSectionTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_master', models.BooleanField(default=False, verbose_name='master template?')),
                ('body', models.ManyToManyField(to='matan.TextSection', blank=True)),
                ('master', models.ForeignKey(related_name='child', blank=True, to='matan.TextSectionTemplate', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('textbodymixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='matan.TextBodyMixin')),
                ('first_name', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('biagrafiya', models.TextField(verbose_name='\u0411\u0438\u0430\u0433\u0440\u0430\u0444\u0438\u044f')),
            ],
            options={
                'ordering': ['last_name'],
            },
            bases=('matan.textbodymixin',),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('textbodymixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='matan.TextBodyMixin')),
                ('title', models.CharField(max_length=100, verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d')),
                ('determination', models.TextField(verbose_name='\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=('matan.textbodymixin',),
        ),
        migrations.CreateModel(
            name='Theorem',
            fields=[
                ('textbodymixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='matan.TextBodyMixin')),
                ('title', models.CharField(max_length=100, verbose_name='\u0422\u0435\u043e\u0440\u0435\u043c\u0430')),
                ('substantiation', models.TextField(verbose_name='\u0414\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e')),
                ('author', models.ManyToManyField(to='matan.Author', verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('term', models.ManyToManyField(to='matan.Term', verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d', blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=('matan.textbodymixin',),
        ),
        migrations.AddField(
            model_name='textbodymixin',
            name='body',
            field=models.ForeignKey(related_name='theorems', blank=True, to='matan.TextSectionTemplate'),
        ),
        migrations.AddField(
            model_name='categories',
            name='term',
            field=models.ManyToManyField(to='matan.Term', verbose_name='\u0422\u0435\u0440\u043c\u0438\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='theorem',
            field=models.ManyToManyField(to='matan.Theorem', verbose_name='\u0422\u0435\u043e\u0440\u0435\u043c\u0430', blank=True),
        ),
    ]
