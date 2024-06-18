from datetime import datetime
from .models import Person
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Person
        fields = [
            'username', 'password'
        ]
        labels = {
            'username': 'Никнейм',
            'password': 'Пароль'
        }
        help_texts = {
            'username': 'Введите никнейм.',
            'password': 'Введите пароль.'
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [
            'username', 'first_name',
            'last_name', 'email', 'password1',
            'password2'
        ]
        lables = {
            'username': 'Никнейм',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'password1': 'Пароль',
            'password2': 'Повторите пароль'
        }
        help_texts = {
            'username': 'Введите никнейм.',
            'first_name': 'Введите имя.',
            'last_name': 'Введите фамилию.',
            'email': 'Введите email.',
            'password1': 'Введите пароль.',
            'password2': 'Повторите пароль.'
        }

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'username', 'first_name', 'last_name',
            'year', 'group', 'description',
            'avatar', 'programming_language',
            'tg_url', 'discord_url', 'github_url',
            'profile_background'
        ]

        labels = {
            'username': 'Никнейм',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'year': 'Год обучения',
            'description': 'Описание',
            'avatar': 'Фото профиля',
            'programming_language': 'Язык программирования',
            'tg_url': 'Telegram',
            'discord_url': 'Discord',
            'github_url': 'Github',
            'profile_background': 'Фон профиля',
            'group': 'Группа'
        }
        help_texts = {
            'username': 'Введите никнейм.',
            'first_name': 'Введите имя.',
            'last_name': 'Введите фамилию.',
            'year': 'Введите год обучения.',
            'description': 'Введите описание.',
            'avatar': 'Загрузите фото профиля.',
            'programming_language': 'Введите язык программирования.',
            'tg_url': 'Введите ссылку на свой Telegram.',
            'discord_url': 'Введите ссылку на свой Discord.',
            'github_url': 'Введите ссылку на свой Github.',
            'profile_background': 'Выберите фон профиля.'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

    def clean_year(self):
        year = self.cleaned_data['year']
        if (year is None) or (year == ''):
            raise forms.ValidationError("Поле год обучения не может быть пустым.")
        current_year = datetime.now().year
        if year > current_year:
            raise forms.ValidationError("Год обучения не может быть больше текущего года.")
        return year
