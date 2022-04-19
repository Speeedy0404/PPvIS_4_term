from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_data = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey('Article', on_delete=models.CASCADE)
