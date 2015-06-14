# -*- coding: utf-8 -*-
from django.contrib import admin
from matan.models import Author, Categories, Term, Theorem, TextSection, Chapter


class TeoremTextInline(admin.TabularInline):
    model = Theorem.text_body.through


class AuthorTextInline(admin.TabularInline):
    model = Author.text_body.through


class TermTextInline(admin.TabularInline):
    model = Term.text_body.through


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')

    inlines = [AuthorTextInline]
    exclude = ('text_body',)


class TheoremAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name')
    search_fields = ['title']

    inlines = [TeoremTextInline]
    exclude = ('text_body', 'term')


class TermAdmin(admin.ModelAdmin):

    inlines = [TermTextInline]
    exclude = ('text_body',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Theorem, TheoremAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Categories)
# admin.site.register(TextSection)
admin.site.register(Chapter)