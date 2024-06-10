from projects.models import Tag, TAGS

for tag_code, tag_name in TAGS:
    Tag.objects.get_or_create(name=tag_code)  # Создаем тег, если он еще не существует

print("Теги успешно добавлены.")