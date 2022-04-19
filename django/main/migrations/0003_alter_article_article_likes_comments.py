# Generated by Django 4.0.4 on 2022-04-19 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
