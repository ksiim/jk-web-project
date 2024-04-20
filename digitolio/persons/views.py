from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Person
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth import login

User = get_user_model()

def test(request):
    return render(request, 'test.html')

def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user': user})

def index(request):
    persons = User.objects.all()
    persons_projects_data = []
    for person in persons:
        projects = person.projects.all()[:3]
        persons_projects_data.append({'person': person, 'projects': projects})
    return render(request, 'users.html', context={'persons_projects_data': persons_projects_data})

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('persons:index')
    template_name = 'registration.html'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)
        login(self.request, self.object)  # log the user in
        return response

@login_required
def profile_update_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = CustomUserUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('persons:profile_view', user_id=user_id)
    return render(request, 'profile_update.html', {'form': form})

@login_required
def person_logout(request):
    logout(request)
    return render(request, 'logged_out.html', {})