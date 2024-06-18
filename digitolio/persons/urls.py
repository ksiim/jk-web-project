from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import CustomUserAuthenticationForm

app_name = 'persons'

urlpatterns = [
    path('update/<str:username>', views.profile_update_view, name='profile_update'),
    path('logout/', views.person_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='persons/login.html', form_class=CustomUserAuthenticationForm), name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('', views.persons, name='persons'),
    path('<str:username>/', views.profile_view, name='profile_view'),
]
