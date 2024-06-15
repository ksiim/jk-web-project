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
    persons = User.objects.all()
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

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('persons:persons')
    template_name = 'persons/registration.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


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
