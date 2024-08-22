from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

class ArticleView(View):
    template_name = "articles/article.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


# def index(request):
#     return render(request, 'articles/article.html', context={})
