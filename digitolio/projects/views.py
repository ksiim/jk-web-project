from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'users.html', context={'projects': projects})

def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        banner = request.POST.get('banner')
        hashtags = request.POST.get('hashtags')
        link_on_code = request.POST.get('link_on_code')
        project = Project.objects.create(
            title=title,
            description=description,
            banner=banner,
            hashtags=hashtags,
            link_on_code=link_on_code
        )
        return render(request, 'project.html', context={'project': project})
    return render(request, 'create_project.html')
