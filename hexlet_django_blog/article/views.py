from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import Http404
from django.views.decorators.http import require_http_methods
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4,
        'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


# @require_http_methods(['GET'])
# def article(request, article_id):
#     for a in articles:
#         if a['id'] == int(article_id):
#             return render(request, 'articles/article.html', context={'article': a})
#     raise Http404()


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')
