from django.shortcuts import get_object_or_404, render
from .models import Project, PROGRAMMING_LANGUAGES, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db.models import Q
from django.forms.models import model_to_dict

def index(request):
    languages = [language[1] for language in PROGRAMMING_LANGUAGES]
    tags = Tag.objects.all()
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/index.html', context={'projects': projects, 'languages': languages, 'tags': tags})

@login_required
def create(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save(commit=False)
        new_project.author = request.user
        new_project.save()
        new_project.tags.set(form.cleaned_data['tags'])
        new_project.save()
        return redirect('projects:index')
    context = {
        'form': form,
        'button_name': 'Добавить проект',
    }
    return render(request, 'projects/create_project.html', context)


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    context = {
        'form': form,
        'button_name': 'Сохранить изменения',
    }
    return render(request, 'projects/create_project.html', context)

@login_required
@csrf_exempt
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_full.html', {'project': project})

def project_data(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_data = {
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'author_full_name': str(project.author.get_full_name()),
        'author_username': project.author.username,
        'author_avatar': project.author.avatar.url if project.author.avatar else '',
        'author_profile_background': project.author.profile_background,
        'created_at': project.created_at.strftime('%d.%m.%Y'),
        'tags': list(project.tags.values_list('name', flat=True)),
        'programming_language': project.get_programming_language_display(),
        'link_on_code': project.link_on_code,
    }
    return JsonResponse(project_data)

@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')
        print(query)
        projects = Project.objects.filter(Q(title__contains=query))
        projects_list = list(projects.values())
        return JsonResponse({'projects': projects_list})
