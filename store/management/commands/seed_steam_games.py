from django.core.management.base import BaseCommand
from store.models import Game, Category
from decimal import Decimal
from datetime import date


class Command(BaseCommand):
    help = 'Добавляет популярные игры из Steam'

    def handle(self, *args, **options):
        # Получаем категории
        shooters = Category.objects.get(slug='shooters')
        strategy = Category.objects.get(slug='strategy')
        rpg = Category.objects.get(slug='rpg')
        racing = Category.objects.get(slug='racing')
        simulators = Category.objects.get(slug='simulators')
        platformers = Category.objects.get(slug='platformers')
        puzzle = Category.objects.get(slug='puzzle')
        adventure = Category.objects.get(slug='adventure')
        sports = Category.objects.get(slug='sports')
        horror = Category.objects.get(slug='horror')

        games = [
            # Шутеры
            {
                'title': 'Counter-Strike 2',
                'description': 'Легендарный тактический шутер от Valve. Бесплатная игра с соревновательными матчами.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/730/header.jpg',
                'category': shooters,
                'developer': 'Valve',
                'publisher': 'Valve',
                'steam_id': '730',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2023, 9, 27)
            },
            {
                'title': 'Call of Duty: Modern Warfare III',
                'description': 'Новая часть легендарной серии Call of Duty с современной графикой и увлекательным сюжетом.',
                'price': Decimal('4999.00'),
                'original_price': Decimal('5999.00'),
                'discount_percent': 17,
                'points_price': 500,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/2519060/header.jpg',
                'category': shooters,
                'developer': 'Sledgehammer Games',
                'publisher': 'Activision',
                'steam_id': '2519060',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2023, 11, 10)
            },
            {
                'title': 'Apex Legends',
                'description': 'Бесплатная королевская битва от создателей Titanfall с уникальными персонажами.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1172470/header.jpg',
                'category': shooters,
                'developer': 'Respawn Entertainment',
                'publisher': 'Electronic Arts',
                'steam_id': '1172470',
                'is_featured': True,
                'release_date': date(2020, 11, 4)
            },
            
            # Стратегии
            {
                'title': 'Age of Empires IV',
                'description': 'Возвращение легендарной серии стратегий в реальном времени с улучшенной графикой.',
                'price': Decimal('1999.00'),
                'original_price': Decimal('2499.00'),
                'discount_percent': 20,
                'points_price': 200,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1466860/header.jpg',
                'category': strategy,
                'developer': 'Relic Entertainment',
                'publisher': 'Xbox Game Studios',
                'steam_id': '1466860',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2021, 10, 28)
            },
            {
                'title': 'Civilization VI',
                'description': 'Классическая пошаговая стратегия о развитии цивилизации от каменного века до будущего.',
                'price': Decimal('999.00'),
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/289070/header.jpg',
                'category': strategy,
                'developer': 'Firaxis Games',
                'publisher': '2K',
                'steam_id': '289070',
                'is_featured': True,
                'release_date': date(2016, 10, 21)
            },
            
            # RPG
            {
                'title': 'The Witcher 3: Wild Hunt',
                'description': 'Эпическая RPG о ведьмаке Геральте в фэнтезийном мире. Одна из лучших игр всех времен.',
                'price': Decimal('1499.00'),
                'original_price': Decimal('1999.00'),
                'discount_percent': 25,
                'points_price': 150,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/292030/header.jpg',
                'category': rpg,
                'developer': 'CD PROJEKT RED',
                'publisher': 'CD PROJEKT RED',
                'steam_id': '292030',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2015, 5, 18)
            },
            {
                'title': 'Elden Ring',
                'description': 'Открытый мир RPG от создателей Dark Souls и Джорджа Мартина. Невероятно сложная и атмосферная игра.',
                'price': Decimal('3999.00'),
                'points_price': 400,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg',
                'category': rpg,
                'developer': 'FromSoftware',
                'publisher': 'Bandai Namco Entertainment',
                'steam_id': '1245620',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2022, 2, 25)
            },
            {
                'title': 'Baldur\'s Gate 3',
                'description': 'Эпическая RPG на основе D&D 5e с глубоким сюжетом и множеством вариантов прохождения.',
                'price': Decimal('2999.00'),
                'points_price': 300,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1086940/header.jpg',
                'category': rpg,
                'developer': 'Larian Studios',
                'publisher': 'Larian Studios',
                'steam_id': '1086940',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2023, 8, 3)
            },
            
            # Гонки
            {
                'title': 'Forza Horizon 5',
                'description': 'Открытый мир аркадных гонок в Мексике с потрясающей графикой и множеством автомобилей.',
                'price': Decimal('2499.00'),
                'points_price': 250,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1551360/header.jpg',
                'category': racing,
                'developer': 'Playground Games',
                'publisher': 'Xbox Game Studios',
                'steam_id': '1551360',
                'is_featured': True,
                'release_date': date(2021, 11, 9)
            },
            
            # Симуляторы
            {
                'title': 'Microsoft Flight Simulator',
                'description': 'Самый реалистичный симулятор полетов с детализированными самолетами и реальными маршрутами.',
                'price': Decimal('1999.00'),
                'points_price': 200,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1250410/header.jpg',
                'category': simulators,
                'developer': 'Asobo Studio',
                'publisher': 'Xbox Game Studios',
                'steam_id': '1250410',
                'is_featured': True,
                'release_date': date(2020, 8, 18)
            },
            
            # Платформеры
            {
                'title': 'Hollow Knight',
                'description': 'Красивая метроидвания с атмосферным миром и сложным геймплеем.',
                'price': Decimal('499.00'),
                'points_price': 50,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/367520/header.jpg',
                'category': platformers,
                'developer': 'Team Cherry',
                'publisher': 'Team Cherry',
                'steam_id': '367520',
                'is_featured': True,
                'release_date': date(2017, 2, 24)
            },
            
            # Головоломки
            {
                'title': 'Portal 2',
                'description': 'Классическая головоломка с порталами и отличным юмором от Valve.',
                'price': Decimal('299.00'),
                'original_price': Decimal('399.00'),
                'discount_percent': 25,
                'points_price': 30,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/620/header.jpg',
                'category': puzzle,
                'developer': 'Valve',
                'publisher': 'Valve',
                'steam_id': '620',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2011, 4, 19)
            },
            
            # Приключения
            {
                'title': 'The Last of Us Part I',
                'description': 'Эмоциональная история о выживании в постапокалиптическом мире. Ремейк классики.',
                'price': Decimal('2999.00'),
                'points_price': 300,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1888930/header.jpg',
                'category': adventure,
                'developer': 'Naughty Dog',
                'publisher': 'Sony Interactive Entertainment',
                'steam_id': '1888930',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2023, 3, 28)
            },
            
            # Спорт
            {
                'title': 'FIFA 24',
                'description': 'Новейшая часть легендарной футбольной серии с улучшенной физикой и графикой.',
                'price': Decimal('2999.00'),
                'original_price': Decimal('3999.00'),
                'discount_percent': 25,
                'points_price': 300,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/2529500/header.jpg',
                'category': sports,
                'developer': 'EA Sports',
                'publisher': 'Electronic Arts',
                'steam_id': '2529500',
                'is_featured': True,
                'is_on_sale': True,
                'is_new': True,
                'release_date': date(2023, 9, 29)
            },
            
            # Хоррор
            {
                'title': 'Resident Evil 4',
                'description': 'Ремейк классического хоррора с современной графикой и улучшенным геймплеем.',
                'price': Decimal('2499.00'),
                'points_price': 250,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/2050650/header.jpg',
                'category': horror,
                'developer': 'CAPCOM',
                'publisher': 'CAPCOM',
                'steam_id': '2050650',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2023, 3, 24)
            },
        ]

        for game_data in games:
            game, created = Game.objects.get_or_create(
                title=game_data['title'],
                defaults=game_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Добавлена игра: {game.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Игра уже существует: {game.title}')
                )
