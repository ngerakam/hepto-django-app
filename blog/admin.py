from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category', 'tag']
    prepopulated_fields = {
        'slug': ['title']
    }
    search_fields = ['title']
    list_display = ['title', 'category_title',
                    'author', 'tag_title', 'date_written']

    def category_title(self, article):
        return article.category.title

    def tag_title(self, article):
        return article.tag.title


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone',  'email']
    list_per_page = 10
    ordering = ['name']
    search_fields = ['name__istartswith', 'email__istartswith']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['featured_article']
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tagged_article']
    list_display = ['title']
    search_fields = ['title']
