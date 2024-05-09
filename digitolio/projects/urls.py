from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('project_data/<int:project_id>/', views.project_data, name='project_data'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    
]