from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from .models import *


class PersonAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Person
    fieldsets = UserAdmin.fieldsets + (
            ('Additional Information', {'fields': ('description', 'experience', 'specialization', 'programming_language')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            ('Additional Information', {'fields': ('description', 'experience', 'specialization', 'programming_language')}),
    )

admin.site.register(Person, PersonAdmin)