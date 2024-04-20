from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]