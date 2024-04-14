from django.shortcuts import render
from .models import Person
from django.http import HttpResponseNotFound


def index(request):
    persons = Person.objects.all()
    persons_projects_data = []
    for person in persons:
        projects = person.projects.all()[:3]
        persons_projects_data.append({'person': person, 'projects': projects})
    print(persons_projects_data)
    return render(request, 'users.html', context={'persons_projects_data': persons_projects_data})


def register_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        person = Person.objects.create(
            name=name,
            email=email,
            password=password
        )
        return render(request, 'person.html', context={'person': person})
    return render(request, 'register_person.html')
