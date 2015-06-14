# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Chapter(models.Model):
    '''
    there some logical text sections for cut text body by some chapters, sectors etc
    '''
    title = models.CharField(max_length=100, verbose_name=u'section')
    section = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.title


class TextSection(models.Model):
    '''
    this is truly text body, for a one chapter
    '''
    text_chapter = models.ForeignKey(Chapter, verbose_name=u'Chapter')
    text = models.TextField(blank=True, null=True)
    editor = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return '%s, by %s' % (self.text_chapter, self.editor)
    

class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Категория')
    text = models.TextField(null=True, verbose_name=u'Текст')
    theorem = models.ManyToManyField('Theorem', verbose_name=u'Теорема', blank=True)
    term = models.ManyToManyField('Term', verbose_name=u'Термин', blank=True)

    def __unicode__(self):
        return self.title


class Theorem(models.Model):
    # https://ru.wikipedia.org/wiki/Категория:Теоремы_математического_анализа
    
    title = models.CharField(max_length=100, verbose_name=u'Теорема')
    substantiation = models.TextField(verbose_name=u'Доказательство')
    text_body = models.ManyToManyField(TextSection, related_name='theorems', blank=True)
    author = models.ManyToManyField('Author', verbose_name=u'Автор')
    term = models.ManyToManyField('Term', verbose_name=u'Термин', blank=True)

    class Meta:
        ordering=['title']

    def author_name(self):
        return '%s' %(u", ".join([author.last_name for author in self.author.all()]))

    def __unicode__(self):
        return self.title

    # def save(self):
    #     for i in Term.objects.all():
    #         if re.search(i.title, self.substantiation):
    #             i.theorem = self
    #             self.terms = True
    #
    # и потом вызывать другой метод, уже в представлениях, который будет отбирать дочерние элементы theorem.term_set.all() и отображать их
    # позже обдумаю - помогу дописать. сейчас уже спать))
    #
    # идея состояла в том, что перед сохранением - выполнить проверку на вхождение в текст имеющихся терминов. и потом, при рендере теоремы
    # во вьюшке - уже знать какие термины находятся внутри, и парсить (разделять текст ради ссылок) только по ним.
    # только идея не совсем идеальна, после сохранения теоремы могут быть добавлены новые термины. которые тоже будут внутри главного текста теоремы
    #
    # скорее всего вся логика ляжет на views


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    biagrafiya = models.TextField(verbose_name=u'Биаграфия')
    text_body = models.ManyToManyField(TextSection, related_name='authors', blank=True)
    # photo = 

    class Meta:
        ordering = ["last_name"]

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Term(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Термин')
    determination = models.TextField(verbose_name=u'Определение')
    text_body = models.ManyToManyField(TextSection, related_name='therms', blank=True)

    class Meta:
        ordering=['title']

    def __unicode__(self):
        return self.title





