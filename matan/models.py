# -*- coding: utf-8 -*-
from django.db import models

<<<<<<< HEAD

class Categories(models.Model):
=======
class Date(models.Model):
    date_pub = models.DateTimeField(null=True, verbose_name='Дата публикации')

    class Meta:
        abstract = True

class Categories(Date):
>>>>>>> 1e4173a4ab3c075334cb1d13522f01a83d04c4f5
    title = models.CharField(max_length=100, verbose_name=u'Категория')
    text = models.TextField(null=True, verbose_name=u'Текст')
    theorem = models.ManyToManyField('Theorem', verbose_name=u'Теорема')
    term = models.ManyToManyField('Term', verbose_name=u'Термин')

    def __unicode__(self):
        return self.title

<<<<<<< HEAD

class Theorem(models.Model):
=======
    class Meta:
        ordering=['title']

class Theorem(Date):
>>>>>>> 1e4173a4ab3c075334cb1d13522f01a83d04c4f5
    title = models.CharField(max_length=100, verbose_name=u'Теорема')
    substantiation = models.TextField(verbose_name=u'Доказательство')
    author = models.ManyToManyField('Author', verbose_name=u'Автор')
    term = models.ManyToManyField('Term', verbose_name=u'Термин')

    def author_name(self):
        return '%s' %(u", ".join([author.last_name for author in self.author.all()]))

    def __unicode__(self):
        return self.title
    '''
    def save(self):
        for i in Term.objects.all():
            if re.search(i.title, self.substantiation):
                i.theorem = self
                self.terms = True

    и потом вызывать другой метод, уже в представлениях, который будет отбирать дочерние элементы theorem.term_set.all() и отображать их
    позже обдумаю - помогу дописать. сейчас уже спать))
    '''


    class Meta:
        ordering=['title']

class Author(Date):
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    biagrafiya = models.TextField(verbose_name=u'Биаграфия')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

<<<<<<< HEAD

class Term(models.Model):
=======
    class Meta:
        ordering=['first_name']

class Term(Date):
>>>>>>> 1e4173a4ab3c075334cb1d13522f01a83d04c4f5
    title = models.CharField(max_length=100, verbose_name=u'Термин')
    determination = models.TextField(verbose_name=u'Определение')
    #theorem = models.ManyToManyField('Theorem', ..)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['title']





