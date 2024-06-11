from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('persons/', include('persons.urls')),
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    # path('profile', include('django.contrib.auth.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
