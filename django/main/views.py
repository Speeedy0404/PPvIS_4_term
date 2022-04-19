from django.shortcuts import render, redirect
from .models import Task, Article, Comments
from .forms import TaskForm, CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


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
        'error': error
    }
    return render(request, 'main/create.html', context)


def articles(request):
    articles = Article.objects.all()
    return render(request, 'main/articles.html', {'title': 'Стена', 'articles': articles})


def article(request, article_id=1):
    comment_form = CommentForm()

    args = {
        'form': comment_form,
        'article': Article.objects.get(id=article_id),
        'comments': Comments.objects.filter(comments_article_id=article_id),
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
