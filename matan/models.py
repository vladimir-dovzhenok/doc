# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Chapter(models.Model):
    '''
    there some logical sections of text that can be placed in other models
    '''
    title = models.CharField(max_length=100, verbose_name=u'section')
    section = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.title


class TextSection(models.Model):
    '''
    the body of the text divided by chapters
    '''
    text_chapter = models.ForeignKey(Chapter, related_name='text_sections', verbose_name=u'Chapter')
    text = models.TextField(blank=True, null=True)
    editor = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return '%s, by %s' % (self.text_chapter, self.editor)


class TextSectionTemplate(models.Model):
    master = models.ForeignKey('self', blank=True, null=True, related_name='child')
    is_master = models.BooleanField(verbose_name=u'master template?', default=False)

    body = models.ManyToManyField(TextSection, blank=True)

    def __unicode__(self):
        preview = 'test' if self.is_master else 'child'
        return preview

    def create_child(self):
        child = TextSectionTemplate.objects.create(master=self)
        for i in self.body.all():
            tmp = TextSection.objects.create(text_chapter=i.text_chapter)
            child.body.add(tmp)
        child.save()
        return child



class TextBodyMixin(models.Model):
    body = models.ForeignKey(TextSectionTemplate, related_name='theorems', blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.body and self.body.is_master:
            self.body = self.body.create_child()
        super(TextBodyMixin, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Категория')
    text = models.TextField(null=True, verbose_name=u'Текст')
    theorem = models.ManyToManyField('Theorem', verbose_name=u'Теорема', blank=True)
    term = models.ManyToManyField('Term', verbose_name=u'Термин', blank=True)

    def __unicode__(self):
        return self.title


class Theorem(TextBodyMixin):
    # https://ru.wikipedia.org/wiki/Категория:Теоремы_математического_анализа

    title = models.CharField(max_length=100, verbose_name=u'Теорема')
    substantiation = models.TextField(verbose_name=u'Доказательство')
    author = models.ManyToManyField('Author', verbose_name=u'Автор')
    term = models.ManyToManyField('Term', verbose_name=u'Термин', blank=True)

    class Meta:
        ordering = ['title']

    def author_name(self):
        return '%s' % (u", ".join([author.last_name for author in self.author.all()]))

    def __unicode__(self):
        return self.title

        # def save(self):
        # for i in Term.objects.all():
        #         if re.search(i.title, self.substantiation):
        #             i.theorem = self
        #             self.terms = True


class Author(TextBodyMixin):
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    biagrafiya = models.TextField(verbose_name=u'Биаграфия')
    # photo =

    class Meta:
        ordering = ["last_name"]

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Term(TextBodyMixin):
    title = models.CharField(max_length=100, verbose_name=u'Термин')
    determination = models.TextField(verbose_name=u'Определение')

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title





