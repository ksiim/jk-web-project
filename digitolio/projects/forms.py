from django import forms
from django_select2.forms import Select2MultipleWidget

from .models import Project, Tag

class ProjectForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=Select2MultipleWidget(attrs={'data-placeholder': 'Выберите теги', 'style': 'width: 100%'}),
        label='Теги'
    )
    class Meta:
        model = Project
        fields = ('title', 'description', 'tags', 'programming_language', 'link_on_code')
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'tags': 'Теги',
            'programming_language': 'Язык программирования',
            'link_on_code': 'Ссылка на гитхаб',
        }
        help_texts = {
            'title': 'Введите название проекта.',
            'description': 'Введите описание проекта.',
            'tags': 'Выберите теги проекта.',
            'programming_language': 'Выберите язык программирования проекта.',
            'link_on_code': 'Введите ссылку на код проекта на гитхабе.',
        }