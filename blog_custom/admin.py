# from blog.models import Article
# from django.contrib import admin
# from django.contrib.contenttypes.admin import GenericTabularInline
# from blog.admin import ArticleAdmin
# from tag.models import TaggedItem


# class TagInline(GenericTabularInline):
#     autocomplete_fields = ['tag']
#     model = TaggedItem


# class CustomArticleAdmin(ArticleAdmin):
#     inlines = [TagInline]


# admin.site.unregister(Article)
# admin.site.register(Article, CustomArticleAdmin)
