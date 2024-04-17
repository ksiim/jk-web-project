from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import *

class PersonAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Person

admin.site.register(Person, PersonAdmin)