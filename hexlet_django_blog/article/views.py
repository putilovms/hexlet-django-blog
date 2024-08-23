from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import View


class ArticleView(View):
    template_name = "articles/article.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


def index(request):
    return redirect(reverse('article_id', kwargs={'tags': 'python', 'article_id': 42}))
