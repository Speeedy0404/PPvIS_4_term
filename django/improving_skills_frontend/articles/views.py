from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

navigation = ["О сайте", "Добавить статью", "Обратная связь", " Войти"]


def index(request):
    post = Articles.objects.all()
    return render(request, 'articles/index.html', {'post': post, 'navigation': navigation, "title": "Главная страница"})


def about(request):
    return render(request, 'articles/about.html', {'navigation': navigation, 'title': 'О сайте'})


def categories(request, cat_id):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'category{cat_id}')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Архив по годам</h1><hp>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
