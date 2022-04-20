from .models import Task, Comments
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название таска'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        widgets = {
            'comments_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите коментарий'})
        }
