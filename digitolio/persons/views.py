from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login

from .models import *
from .forms import CustomUserCreationForm, CustomUserUpdateForm


User = get_user_model()


def persons(request):
    groups = Group.objects.all()
    persons = [user for user in User.objects.all() if user.role == 'student']
    languages = [language[1] for language in PROGRAMMING_LANGUAGES]
    persons_projects_data = []
    for person in persons:
        if person.programming_language:
            person.programming_language = person.programming_language.capitalize()
        projects = person.projects.all()[:3]
        persons_projects_data.append({'person': person, 'projects': projects, 'groups': groups})
    return render(request, 'persons/persons.html', context={'persons_projects_data': persons_projects_data, 'groups': groups, 'languages': languages, 'languages_dict': dict(PROGRAMMING_LANGUAGES)})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'persons/profile.html', {'user': user})

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('persons:persons'))
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'persons/registration.html', {'form': form})


@login_required(login_url='persons:login')
def profile_update_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('persons:profile_view', username=username)
    else:
        form = CustomUserUpdateForm(instance=user)
    return render(request, 'persons/profile_update.html', {'form': form})


@login_required(login_url='persons:login')
def person_logout(request):
    logout(request)
    return render(request, 'persons/logged_out.html', {})
