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
            'username', 'first_name', 'last_name', 'description',
            'experience', 'specialization',
            'programming_language'
        ]

        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'description': 'Описание',
            'experience': 'Опыт работы',
            'specialization': 'Специалтзация',
            'programming_language': 'Язык программирования'
        }
        help_texts = {
            'username': 'Введите имя пользователя.',
            'first_name': 'Введите имя.',
            'last_name': 'Введите фамилию.',
            'description': 'Введите описание.',
            'experience': 'Введите опыт работы.',
            'specialization': 'Введите специализацию.',
            'programming_language': 'Введите язык программирования.'
        }
