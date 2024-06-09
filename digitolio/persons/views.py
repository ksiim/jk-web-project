from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login

from .forms import CustomUserCreationForm, CustomUserUpdateForm


User = get_user_model()


def persons(request):
    persons = User.objects.all()
    persons_projects_data = []
    for person in persons:
        projects = person.projects.all()[:3]
        persons_projects_data.append({'person': person, 'projects': projects})
    return render(request, 'persons/persons.html', context={'persons_projects_data': persons_projects_data})


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
    form = CustomUserUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('persons:profile_view', username=username)
    return render(request, 'persons/profile_update.html', {'form': form})


@login_required(login_url='persons:login')
def person_logout(request):
    logout(request)
    return render(request, 'persons/logged_out.html', {})
