from django.shortcuts import render
from .models import Person
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    users = Person.objects.select_related("projects").all()
    return render(request, 'users.html', context={'users': users})
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
