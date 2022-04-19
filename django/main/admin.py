from django.contrib import admin

# Register your models here.
from .models import Task, Article, Comments


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_data']
    inlines = [ArticleInline]
    list_filter = ['article_data']


admin.site.register(Task)
admin.site.register(Article, ArticleAdmin)
