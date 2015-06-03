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
    model=Author
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
    def get(self, request):
        if 'q' in request.GET:
            q = request.GET['q']
        #называть переменные одной буквой - дурной тон. со временем не понять зачем эта переменная была создана
        #занимается поиском - search, содержит результат - result, и т.д 
        #английский хотябы здесь пригодится. хотя и дальше тоже

        poisk = Theorem.objects.filter(title__icontains=q)
        if not poisk:
            poisk = Term.objects.filter(title__icontains=q)
        if not poisk:
            poisk = Author.objects.filter(last_name__icontain
        '''
            хотелось бы, чтобы поиск вёлся не по условию отсечения, а сразу по всем таблицам. т.е. введённое слово на сайте будет
            разыскиваться по всем полезным моделям (теорема, термин, автор)
            в одну строчку это может быть и не сделать, но можно делать последовательные запросы, а результат добавлять в общую
            переменную - хранилище, нарпример в list. и в результате добавить его в context
        '''
        return render_to_response('matan/poisk.html', {'poisk': poisk, 'query': q})

        '''
        вообще, ты немного не верно понимаешь принципы разделения обязанностей в методах классов.
        смысл в том - что get будет только лишь обрабатывать входящие данные, post будет обрабатывать запросы на измененния данных,
        get_context_data метод - будет использоваться чтобы подбросить в контекст то, что нам нужно.. и т.д

        т.е. правильная реализация этой задачи будет выглядеть

        class Имя_класса(наследование):

            def get(self):
                if 'q' in request.GET:
                    self.search_field = request.GET['q']
                return super(Имя_класса, self).get(self)

            def get_context_data(self)
                context = super(Имя_класса, self).get_context_data(self)

                место нахождения обьектов по self.search_field
                context['result'] = результат поиска по бд
                return context
        '''


def base(request):
    base=Theorem.objects.all()[:3]
    return render_to_response('matan/base.html', {'base': base})
'''
def alfa(request):
    list = []
    list = Theorem.objects.all()[0]
    for i in list
        i.list.

------------------------------------------------------------------
если ты хотел проработать алфавит, то чуть интереснее будет оформить его так:

class Имя_класса_который_рендерит_страницу_где_будет_алфавит(наследование):
    template = 'шаблон'

    def get_context_data(self):
        context = super(Имя_класса_который_рендерит_страницу_где_будет_алфавит, self).get_context_data(self)

        alpha_context = {}
        alphabit = 'каким то образом создаёшь алфавит, только интерируемый, т.е. который можно обойти циклом'
        for i in alphabit:
            result =  Theorem.objects.filter(title__istartswith=i)
            if result:
                alpha_context[i] = result

        context['alphabit_dict'] = alpha_context
        return context

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

только вот не уверен за alpha_context[alpha] внутри шаблона.. может быть придётся брать доступ по ключу иначе.
выходит так в цикле {% for alpha in alpha_context %} мы перебираем не значения, а ключи словаря. а чтобы получить значения -
нужно обратиться к словарю через ключ: alpha_context[alpha]
но результат тоже будет итериремым, query-set`ом, который практически идентичен list. вот для обхода всех его значений и
используется второй цикл. пусть даже там помещен всего один обьект, заранее ведь не знаем.

-------------------------------------------------------------------

def poisk(request):
    if 'q' in request.GET:
        q = request.GET['q']
        poisk = Term.objects.filter(titli__icontains=q)
    return render_to_response('matan/poisk.html', {'poisk': poisk, 'query': q})
'''

