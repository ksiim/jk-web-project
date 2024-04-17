from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('projects.urls')),
    path('persons/', include('persons.urls')),
    path('admin/', admin.site.urls),
    path('profile', include('django.contrib.auth.urls'))
]
