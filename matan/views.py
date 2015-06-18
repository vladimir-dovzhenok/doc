# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Q
from django.shortcuts import render_to_response
from django.views.generic import View, ListView, DetailView
from matan.models import Theorem, Term, Categories, Author


class AuthorView(ListView):
    model = Author
    template_name = 'matan/author.html'
    context_object_name = 'author_list'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'matan/author_detail.html'
    context_object_name = 'author'


class TheoremView(ListView):
    model = Theorem
    template_name = 'matan/theorem_list.html'
    context_object_name = 'theorem_list'


class TheoremDetail(DetailView):
    model = Theorem
    template_name = 'matan/theorem_detail.html'
    context_object_name = 'theorem'


class TermView(ListView):
    model = Term
    template_name = 'matan/term_list.html'
    context_object_name = 'term_list'


class TermDetail(DetailView):
    model = Term
    template_name = 'matan/term_detail.html'
    context_object_name = 'term'


class CategoriesView(ListView):
    model = Categories
    template_name = 'matan/categories.html'
    context_object_name = 'categories_list'


class CategoriesDetail(DetailView):
    model = Categories
    template_name = 'matan/categories_detail.html'
    context_object_name = 'categories'


class SearchView(View):
    def get(self, request):
        if 'search-input' in request.GET:
            search = request.GET['search-input']
        # называть переменные одной буквой - дурной тон. со временем не понять зачем эта переменная была создана
        #занимается поиском - search, содержит результат - result, и т.д 
        #английский хотябы здесь пригодится. хотя и дальше тоже

        result = Theorem.objects.filter(title__icontains=search)
        if not result:
            result = Term.objects.filter(title__icontains=search)
        if not result:
            result = Author.objects.filter(last_name__icontains=search)
        return render_to_response('matan/search.html', {'result': result, 'search-input': search})


def base(request):
    base = Theorem.objects.all()[:3]
    return render_to_response('matan/base.html', {'base': base})

#если ты хотел проработать алфавит, то чуть интереснее будет оформить его так:
'''
def alpha(request):

        alphabet = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й',
                    'К','Л','М','Н','О','П','Р','С','Т','У','Ф',
                    'Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я',
                    'а','б','в','г','д','е','ё','ж','з','и','й',
                    'к','л','м','н','о','п','р','с','т','у','ф',
                    'х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',]

        for i in range(65,123):
            if 'a'<=chr(i)<='z' or 'A'<=chr(i)<='Z':
                alphabet_english = chr(i)
                alphabet.append(alphabet_english)
        return render_to_response('matan/theorem_list.html', {'alpha': alphabet})
'''
class Alphabet(View):
    template_name = 'matan/alphabet.html'

    def get_context_data(self):
        context = super(Alphabet, self).get_context_data(self)

        alpha_context = {}

        alphabet = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й',
                    'К','Л','М','Н','О','П','Р','С','Т','У','Ф',
                    'Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я',
                    'а','б','в','г','д','е','ё','ж','з','и','й',
                    'к','л','м','н','о','п','р','с','т','у','ф',
                    'х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',]
        for n in range(65,123):
            if 'a'<=chr(n)<='z' or 'A'<=chr(n)<='Z':
                alphabet_english = chr(n)
                alphabet.append(alphabet_english)

        for i in alphabet:
            result = Theorem.objects.filter(title__istartswith=i)
            if result:
                alpha_context[i] = result

        context['alphabet_dict'] = alpha_context
        return context
'''
вроде как должно работать. не обижайся, что написал за тебя. будет ещё много фишек, на которых будешь учится.
alphabit_dict можно будет использовать циклом в шаблоне и ключ использовать в качестве буквы алфавита, допустим так:

{% for alpha in alpha_context %}
    <h3>{{}}</h3>
    <ul>
        {% for field in alpha_context[alpha] %}
        <li>{{ field }}</li>
        {% endfor %}
    </ul>
{% endfor %}

for i in range(65,123):
            if 'a'<=chr(i)<='z' or 'A'<=chr(i)<='Z':
только вот не уверен за alpha_context[alpha] внутри шаблона.. может быть придётся брать доступ по ключу иначе.
выходит так в цикле {% for alpha in alpha_context %} мы перебираем не значения, а ключи словаря. а чтобы получить значения -
нужно обратиться к словарю через ключ: alpha_context[alpha]
но результат тоже будет итериремым, query-set`ом, который практически идентичен list. вот для обхода всех его значений и
используется второй цикл. пусть даже там помещен всего один обьект, заранее ведь не знаем.




def poisk(request):
    if 'q' in request.GET:
        q = request.GET['q']
        poisk = Term.objects.filter(titli__icontains=q)
    return render_to_response('matan/poisk.html', {'poisk': poisk, 'query': q})
 for i in range(1,100000):
        if 'a'<=chr(i)<='z' or 'A'<=chr(i)<='Z':
            return render_to_response('matan/alfa.html', {'chr': chr(i)})
'''

