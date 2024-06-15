import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitolio.settings')
django.setup()

from projects.models import Tag, TAGS

for tag_code, tag_name in TAGS:
    Tag.objects.get_or_create(name=tag_code)  # Создаем тег, если он еще не существует

print("Теги успешно добавлены.")
