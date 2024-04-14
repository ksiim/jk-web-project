from django.urls import path
from . import views

app_name = 'persons'

urlpatterns = [
    path('', views.index, name='persons_index'),
]