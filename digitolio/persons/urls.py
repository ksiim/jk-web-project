from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'persons'

urlpatterns = [
    path('update/<str:username>', views.profile_update_view, name='profile_update'),
    path('logout/', views.person_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='persons/login.html'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.persons, name='persons'),
    path('<str:username>/', views.profile_view, name='profile_view'),
    

    # path('password_change/', PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'),
    # path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    # path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
