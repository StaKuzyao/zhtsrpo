from django.core.management.base import BaseCommand
from store.models import Game, Category
from decimal import Decimal
from datetime import date


class Command(BaseCommand):
    help = 'Заменяет FIFA 24 на другую игру из Steam'

    def handle(self, *args, **options):
        try:
            # Удаляем FIFA 24
            fifa = Game.objects.get(title='FIFA 24')
            fifa.delete()
            self.stdout.write(
                self.style.SUCCESS('FIFA 24 удалена')
            )
        except Game.DoesNotExist:
            self.stdout.write(
                self.style.WARNING('FIFA 24 не найдена')
            )

        # Получаем категорию для спорта
        try:
            sports = Category.objects.get(slug='sports')
        except Category.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Категория "Спорт" не найдена')
            )
            return

        # Добавляем новую игру - Rocket League (бесплатная игра)
        rocket_league_data = {
            'title': 'Rocket League',
            'description': 'Футбол на автомобилях! Бесплатная игра с уникальным геймплеем, где вы играете в футбол, управляя ракетными автомобилями. Невероятно веселая и захватывающая игра для всех возрастов.',
            'price': Decimal('0.00'),
            'points_price': 0,
            'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/252950/header.jpg',
            'category': sports,
            'developer': 'Psyonix',
            'publisher': 'Psyonix',
            'steam_id': '252950',
            'is_featured': True,
            'is_new': False,
            'release_date': date(2015, 7, 7)
        }

        # Создаем новую игру
        rocket_league, created = Game.objects.get_or_create(
            title=rocket_league_data['title'],
            defaults=rocket_league_data
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Добавлена новая игра: {rocket_league.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Игра уже существует: {rocket_league.title}')
            )

        # Также добавим еще одну популярную игру - Among Us
        try:
            puzzle = Category.objects.get(slug='puzzle')
        except Category.DoesNotExist:
            puzzle = sports  # Fallback

        among_us_data = {
            'title': 'Among Us',
            'description': 'Мультиплеерная игра на выживание в космосе! Работайте вместе, чтобы найти предателя среди экипажа, или саботируйте миссию, если вы самозванец. Идеальная игра для вечеринок с друзьями.',
            'price': Decimal('199.00'),
            'original_price': Decimal('299.00'),
            'discount_percent': 33,
            'points_price': 20,
            'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/945360/header.jpg',
            'category': puzzle,
            'developer': 'InnerSloth',
            'publisher': 'InnerSloth',
            'steam_id': '945360',
            'is_featured': True,
            'is_on_sale': True,
            'is_new': False,
            'release_date': date(2018, 11, 16)
        }

        among_us, created = Game.objects.get_or_create(
            title=among_us_data['title'],
            defaults=among_us_data
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Добавлена новая игра: {among_us.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Игра уже существует: {among_us.title}')
            )

        self.stdout.write(
            self.style.SUCCESS('\nЗамена завершена!')
        )
