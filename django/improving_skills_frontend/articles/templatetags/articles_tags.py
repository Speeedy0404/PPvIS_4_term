from django import template
from articles.models import *
from articles.views import navigation

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('articles/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('articles/list_main_menu.html')
def show_menu():
    return {'navigation': navigation}
