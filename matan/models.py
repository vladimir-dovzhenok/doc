# -*- coding: utf-8 -*-
from django.db import models

class Date(models.Model):
    date_pub = models.DateTimeField(null=True, verbose_name='Дата публикации')

    class Meta:
        abstract = True

class Categories(Date):
    title = models.CharField(max_length=100, verbose_name=u'Категория')
    text = models.TextField(null=True, verbose_name=u'Текст')
    theorem = models.ManyToManyField('Theorem', verbose_name=u'Теорема')
    term = models.ManyToManyField('Term', verbose_name=u'Термин')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['title']

class Theorem(Date):
    title = models.CharField(max_length=100, verbose_name=u'Теорема')
    substantiation = models.TextField(verbose_name=u'Доказательство')
    author = models.ManyToManyField('Author', verbose_name=u'Автор')
    term = models.ManyToManyField('Term', verbose_name=u'Термин')

    def author_name(self):
        return '%s' %(u", ".join([author.last_name for author in self.author.all()]))

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['title']

class Author(Date):
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    biagrafiya = models.TextField(verbose_name=u'Биаграфия')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering=['first_name']

class Term(Date):
    title = models.CharField(max_length=100, verbose_name=u'Термин')
    determination = models.TextField(verbose_name=u'Определение')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['title']





