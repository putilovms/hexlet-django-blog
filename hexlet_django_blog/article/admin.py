from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Перечисляем поля, отображаемые в таблице списка статей
    list_display = ('name', 'created_at')
    search_fields = ['name', 'body']
    # Перечисляем поля для фильтрации
    list_filter = (('created_at', DateFieldListFilter),)
