# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView
from matan.models import Author, Theorem, Term
from matan import views

urlpatterns = patterns('',
    url(r'^$', views.TheoremView.as_view(
        model=Theorem,
        template_name='matan/base.html',
        context_object_name='theorem_list'), name='base'),
    url(r'^author/$', views.AuthorView.as_view(), name='author_list'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
    url(r'^theorem/$', views.TheoremView.as_view(), name='theorem_list'),
    url(r'^theorem/(?P<pk>\d+)/$', views.TheoremDetail.as_view(), name='theorem_detail'),
    url(r'^term/$', views.TermView.as_view(), name='term_list'),
    url(r'^term/(?P<pk>\d+)$', views.TermDetail.as_view(), name='term_detail'),
    url(r'^poisk/$', views.PoiskView.as_view()),
    url(r'^categories/$', views.CategoriesView.as_view(), name='categories_list'),
    url(r'^categories/(?P<pk>\d+)$', views.CategoriesDetail.as_view(), name='categories_detail'),
    )