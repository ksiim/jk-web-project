import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitolio.settings')
django.setup()

from projects.models import Tag, TAGS
from persons.models import Group

for tag_code, tag_name in TAGS:
    Tag.objects.get_or_create(name=tag_code)  # Создаем тег, если он еще не существует

[Group.objects.get_or_create(name=f"AT-{number:02}") for number in range(1, 10)]

print("Теги и группы успешно добавлены.")