from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'category', 'programming_language', 'link_on_code')
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'category': 'Категория',
            'programming_language': 'Язык программирования',
            'link_on_code': 'Ссылка на гитхаб',
        }
        help_texts = {
            'title': 'Введите название проекта.',
            'description': 'Введите описание проекта.',
            'category': 'Выберите категорию проекта.',
            'programming_language': 'Выберите язык программирования проекта.',
            'link_on_code': 'Введите ссылку на код проекта на гитхабе.',
        }