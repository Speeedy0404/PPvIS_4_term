from django.shortcuts import render, redirect
from .models import Task, Article, Comments
from .forms import TaskForm


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
    article = Article.objects.get(id=article_id)
    return render(request, 'main/article.html',
                  {'title': 'Статья', 'article': article,
                   'comments': Comments.objects.filter(comments_article_id=article_id)})
