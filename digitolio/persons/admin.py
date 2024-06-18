from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import Person, Group as CustomGroup


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    verbose_name = "Группа"
    verbose_name_plural = "Группы"

class PersonAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Person

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
            ('Additional Information', {'fields': ('description',  'programming_language', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            ('Additional Information', {'fields': ('description',  'programming_language')}),
    )

admin.site.site_header = 'Digitolio - Панель администратора'

admin.site.unregister(Group)

admin.site.register(CustomGroup, GroupAdmin)
admin.site.register(Person, PersonAdmin)