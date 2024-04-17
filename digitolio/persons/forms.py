from .models import Person
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [
            'username', 'email', 'password1',
            'password2', 'description',
            'experience', 'specialization',
            'programming_language'
        ]