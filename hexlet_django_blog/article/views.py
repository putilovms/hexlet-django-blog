from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import Http404
from django.views.decorators.http import require_http_methods

articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]


class ArticleView(View):
    template_name = "articles/article.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


def index(request):
    return redirect(reverse('article_id', kwargs={'tags': 'python', 'article_id': 42}))


@require_http_methods(['GET'])
def article(request, article_id):
    for a in articles:
        if a['id'] == int(article_id):
            return render(request, 'articles/article.html', context={'article': a})
    raise Http404()
