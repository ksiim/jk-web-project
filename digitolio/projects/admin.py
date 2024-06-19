from django.contrib import admin

from .models import Tag, Project

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    verbose_name = "Тег"
    verbose_name_plural = "Теги"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'programming_language', 'created_at', 'updated_at', 'grade')
    search_fields = ('title', 'author__username', 'programming_language', 'description')
    list_filter = ('programming_language', 'tags', 'created_at', 'updated_at', 'grade')
    ordering = ('-created_at',)

    verbose_name = "Проект"
    verbose_name_plural = "Проекты"

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)