from django.shortcuts import render, redirect
from .models import Task, Article, Comments
from .forms import TaskForm, CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.contrib import auth
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'tasks': tasks, 'username': auth.get_user(request).username})


def about(request):
    return render(request, 'main/about.html', {'username': auth.get_user(request).username})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'
    form = TaskForm()

    context = {
        'form': form,
        'error': error,
        'username': auth.get_user(request).username
    }
    return render(request, 'main/create.html', context)


def articles(request, page_number=1):
    articles = Article.objects.all()
    current_page = Paginator(articles, 3)
    return render(request, 'main/articles.html',
                  {'title': 'Стена', 'articles': current_page.page(page_number),
                   'username': auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm()

    args = {
        'form': comment_form,
        'article': Article.objects.get(id=article_id),
        'comments': Comments.objects.filter(comments_article_id=article_id),
        'username': auth.get_user(request).username,
    }

    return render(request, 'main/article.html', args)


def add_like(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            responce = redirect('articles')
            responce.set_cookie(article_id, 'like')
            return responce
    except ObjectDoesNotExist:
        raise Http404
    return redirect('articles')


def add_comment(request, article_id):
    if request.method == 'POST' and ("pause" not in request.session):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment_form.save()
            request.session.set_expiry(600)
            request.session['pause'] = True

    return redirect('/articles/get/%s/' % article_id)
