# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Q
from django.shortcuts import render_to_response
from django.views.generic import View, ListView, DetailView
from matan.models import Theorem, Term, Categories, Author

class AuthorView(ListView):
    model=Author
    template_name='matan/author.html'
    context_object_name='author_list'

class AuthorDetail(DetailView):
    mdocodel=Author
    template_name='matan/author_detail.html'
    context_object_name='author'

class TheoremView(ListView):
    model=Theorem
    template_name='matan/theorem_list.html'
    context_object_name='theorem_list'

class TheoremDetail(DetailView):
    model=Theorem
    template_name='matan/theorem_detail.html'
    context_object_name='theorem'

class TermView(ListView):
    model=Term
    template_name='matan/term_list.html'
    context_object_name='term_list'



class TermDetail(DetailView):
    model=Term
    template_name='matan/term_detail.html'
    context_object_name='term'

class CategoriesView(ListView):
    model=Categories
    template_name='matan/categories.html'
    context_object_name='categories_list'

class CategoriesDetail(DetailView):
    model=Categories
    template_name='matan/categories_detail.html'
    context_object_name='categories'

class PoiskView(View):
    def get(self, request, q=''):
        poisk=[]
        if 'q' in request.GET:
            q = request.GET['q']
        if not poisk:
                poisk=Theorem.objects.filter(title__icontains=q)
        if not poisk:
                poisk=Term.objects.filter(title__icontains=q)
        if not poisk:
                poisk=Author.objects.filter(Q(last_name__icontains=q)|Q(first_name__icontains=q))
        return render_to_response('matan/poisk.html', {'poisk': poisk, 'query': q})


def base(request):
    base=Theorem.objects.all()[:3]
    return render_to_response('matan/base.html', {'base': base})


def alfa(request):
    list = Theorem.objects.all()
    for i in list:
        return render_to_response('matan/alfa.html', {'i': i, 'list': list})


'''
def poisk(request):
    if 'q' in request.GET:
        q = request.GET['q']
        poisk = Term.objects.filter(titli__icontains=q)
    return render_to_response('matan/poisk.html', {'poisk': poisk, 'query': q})
 for i in range(1,100000):
        if 'a'<=chr(i)<='z' or 'A'<=chr(i)<='Z':
            return render_to_response('matan/alfa.html', {'chr': chr(i)})
'''

