from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *

navigation = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


class ArticlesHome(ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Articles.objects.filter(is_published=True)


"""
def index(request):
    posts = Articles.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'articles/index.html', context=context)
"""


def about(request):
    return render(request, 'articles/about.html', {'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'articles/addpage.html'

    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


"""
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, 'articles/addpage.html', {'form': form, 'title': 'Добавление статьи'})
"""


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


class ShowPost(DetailView):
    model = Articles
    template_name = 'articles/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['cat_selected'] = context['post'].cat_id
        return context


"""
def show_post(request, post_slug):
    post = get_object_or_404(Articles, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'articles/post.html', context=context)
"""


class ArticlesCategory(ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Articles.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


"""
def show_category(request, cat_slug):
    cat = Category.objects.get(slug=cat_slug)
    posts = Articles.objects.filter(cat_id=cat.id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat.id,
    }
    return render(request, 'articles/index.html', context=context)
"""


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
