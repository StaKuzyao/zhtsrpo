from django.core.management.base import BaseCommand
from store.models import Category


class Command(BaseCommand):
    help = 'Создает базовые категории игр'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Шутеры', 'slug': 'shooters', 'description': 'Игры с акцентом на стрельбу и боевые действия'},
            {'name': 'Стратегии', 'slug': 'strategy', 'description': 'Стратегические игры, требующие планирования и тактики'},
            {'name': 'RPG', 'slug': 'rpg', 'description': 'Ролевые игры с развитием персонажа'},
            {'name': 'Гонки', 'slug': 'racing', 'description': 'Автомобильные и мотоциклетные гонки'},
            {'name': 'Симуляторы', 'slug': 'simulators', 'description': 'Симуляторы различных видов деятельности'},
            {'name': 'Платформеры', 'slug': 'platformers', 'description': 'Игры с прыжками по платформам'},
            {'name': 'Головоломки', 'slug': 'puzzle', 'description': 'Логические игры и головоломки'},
            {'name': 'Приключения', 'slug': 'adventure', 'description': 'Приключенческие игры с исследованием мира'},
            {'name': 'Спорт', 'slug': 'sports', 'description': 'Спортивные симуляторы'},
            {'name': 'Хоррор', 'slug': 'horror', 'description': 'Ужасы и игры с атмосферой страха'},
        ]

        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Создана категория: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Категория уже существует: {category.name}')
                )
