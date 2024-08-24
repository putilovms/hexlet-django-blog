from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path('<str:tags>/<int:article_id>', views.ArticleView.as_view(), name='article_id'),
    path('<int:article_id>/', views.article),
    path('', views.index),
]