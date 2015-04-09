# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView
#from matan.models import Author, Theorem, Cat, Term
from matan import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(
        template_name='matan/base.html'), name='base'),
    url(r'^author/$', views.AuthorView.as_view()),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
    url(r'^theorem/$', views.TheoremView.as_view()),
    url(r'^theorem/(?P<pk>\d+)/$', views.TheoremDetail.as_view(), name='theorem_detail'),
    url(r'^term/$', views.TermView.as_view()),
    url(r'^term/(?P<pk>\d+)$', views.TermDetail.as_view(), name='term_detail'),
    url(r'^poisk/$', views.PoiskView.as_view()),
    url(r'^categories/$', views.CategoriesView.as_view(), name='categories_list'),
    url(r'^categories/(?P<pk>\d+)$', views.CategoriesDetail.as_view(), name='categories_detail'),
    )