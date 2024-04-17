from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import CustomUserCreationForm, Person
from django.http import HttpResponseNotFound
from django.contrib.auth import login
from django.views.generic.edit import CreateView


def index(request):
    persons = Person.objects.all()
    persons_projects_data = []
    for person in persons:
        projects = person.projects.all()[:3]
        persons_projects_data.append({'person': person, 'projects': projects})
    return render(request, 'users.html', context={'persons_projects_data': persons_projects_data})
    # return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/persons')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration.html', {'form': form})

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('projects:index')
    template_name = 'registration.html'