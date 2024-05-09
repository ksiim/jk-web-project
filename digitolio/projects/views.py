from django.shortcuts import get_object_or_404, render
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', context={'projects': projects})

@login_required
def create(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save(commit=False)
        new_project.author = request.user
        new_project.save()
        return redirect('projects:index')
    context = {
        'form': form,
        'button_name': 'Добавить проект',
    }
    return render(request, 'projects/create_project.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')
        print(query)
        projects = Project.objects.filter(Q(title__contains=query))
        projects_list = list(projects.values())
        return JsonResponse({'projects': projects_list})
