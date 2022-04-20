from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('articles', views.articles, name='articles'),
    re_path(r'^articles/get/(?P<article_id>\d+)/$', views.article),
    re_path(r'^articles/addlike/(?P<article_id>\d+)/$', views.add_like),
    re_path(r'^articles/addcomment/(?P<article_id>\d+)/$', views.add_comment),
    re_path(r'^page/(\d+)/$', views.articles)

]
