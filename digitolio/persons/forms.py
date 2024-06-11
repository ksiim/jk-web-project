from .models import Person
from django import forms
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [
            'username', 'email', 'password1',
            'password2'
        ]

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'username', 'first_name', 'last_name',
            'year', 'team', 'description',
            'avatar', 'programming_language',
            'tg_url', 'discord_url', 'github_url',
            'profile_background'
        ]

        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'year': 'Год обучения',
            'team': 'Команда',
            'description': 'Описание',
            'avatar': 'Фото профиля',
            'programming_language': 'Язык программирования',
            'tg_url': 'Telegram',
            'discord_url': 'Discord',
            'github_url': 'Github',
            'profile_background': 'Фон профиля'
        }
        help_texts = {
            'username': 'Введите имя пользователя.',
            'first_name': 'Введите имя.',
            'last_name': 'Введите фамилию.',
            'year': 'Введите год обучения.',
            'team': 'Введите команду.',
            'description': 'Введите описание.',
            'avatar': 'Загрузите фото профиля.',
            'programming_language': 'Введите язык программирования.',
            'tg_url': 'Введите ссылку на свой Telegram.',
            'discord_url': 'Введите ссылку на свой Discord.',
            'github_url': 'Введите ссылку на свой Github.',
            'profile_background': 'Выберите фон профиля.'
        }
