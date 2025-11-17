from django.core.management.base import BaseCommand
from store.models import Game, Category
from decimal import Decimal
from datetime import date


class Command(BaseCommand):
    help = 'Добавляет больше игр с картинками'

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
            # Дополнительные шутеры
            {
                'title': 'Valorant',
                'description': 'Бесплатная тактическая командная игра от Riot Games с уникальными агентами.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1276090/header.jpg',
                'category': shooters,
                'developer': 'Riot Games',
                'publisher': 'Riot Games',
                'steam_id': '1276090',
                'is_featured': True,
                'release_date': date(2020, 6, 2)
            },
            {
                'title': 'Overwatch 2',
                'description': 'Бесплатная командная шутер с героями и уникальными способностями.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/2357570/header.jpg',
                'category': shooters,
                'developer': 'Blizzard Entertainment',
                'publisher': 'Blizzard Entertainment',
                'steam_id': '2357570',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2022, 10, 4)
            },
            {
                'title': 'Destiny 2',
                'description': 'Бесплатная MMO-шутер с кооперативными рейдами и PvP.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1085660/header.jpg',
                'category': shooters,
                'developer': 'Bungie',
                'publisher': 'Bungie',
                'steam_id': '1085660',
                'is_featured': True,
                'release_date': date(2019, 10, 1)
            },
            
            # Дополнительные стратегии
            {
                'title': 'Total War: Warhammer III',
                'description': 'Эпическая стратегия в реальном времени в мире Warhammer Fantasy.',
                'price': Decimal('2499.00'),
                'original_price': Decimal('2999.00'),
                'discount_percent': 17,
                'points_price': 250,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1142710/header.jpg',
                'category': strategy,
                'developer': 'Creative Assembly',
                'publisher': 'SEGA',
                'steam_id': '1142710',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2022, 2, 17)
            },
            {
                'title': 'Crusader Kings III',
                'description': 'Глубокая средневековая стратегия с династиями и интригами.',
                'price': Decimal('1999.00'),
                'points_price': 200,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1158310/header.jpg',
                'category': strategy,
                'developer': 'Paradox Development Studio',
                'publisher': 'Paradox Interactive',
                'steam_id': '1158310',
                'is_featured': True,
                'release_date': date(2020, 9, 1)
            },
            
            # Дополнительные RPG
            {
                'title': 'Cyberpunk 2077',
                'description': 'Открытый мир RPG в киберпанк-будущем от создателей The Witcher.',
                'price': Decimal('1999.00'),
                'original_price': Decimal('2499.00'),
                'discount_percent': 20,
                'points_price': 200,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1091500/header.jpg',
                'category': rpg,
                'developer': 'CD PROJEKT RED',
                'publisher': 'CD PROJEKT RED',
                'steam_id': '1091500',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2020, 12, 10)
            },
            {
                'title': 'Divinity: Original Sin 2',
                'description': 'Классическая изометрическая RPG с глубокой системой боя.',
                'price': Decimal('999.00'),
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/435150/header.jpg',
                'category': rpg,
                'developer': 'Larian Studios',
                'publisher': 'Larian Studios',
                'steam_id': '435150',
                'is_featured': True,
                'release_date': date(2017, 9, 14)
            },
            
            # Дополнительные гонки
            {
                'title': 'Gran Turismo 7',
                'description': 'Реалистичный симулятор автогонок с потрясающей графикой.',
                'price': Decimal('2999.00'),
                'points_price': 300,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1446780/header.jpg',
                'category': racing,
                'developer': 'Polyphony Digital',
                'publisher': 'Sony Interactive Entertainment',
                'steam_id': '1446780',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2022, 3, 4)
            },
            {
                'title': 'Dirt Rally 2.0',
                'description': 'Реалистичный симулятор ралли с отличной физикой.',
                'price': Decimal('1499.00'),
                'original_price': Decimal('1999.00'),
                'discount_percent': 25,
                'points_price': 150,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/690790/header.jpg',
                'category': racing,
                'developer': 'Codemasters',
                'publisher': 'Codemasters',
                'steam_id': '690790',
                'is_on_sale': True,
                'release_date': date(2019, 2, 26)
            },
            
            # Дополнительные симуляторы
            {
                'title': 'Euro Truck Simulator 2',
                'description': 'Реалистичный симулятор грузовика по дорогам Европы.',
                'price': Decimal('499.00'),
                'points_price': 50,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/227300/header.jpg',
                'category': simulators,
                'developer': 'SCS Software',
                'publisher': 'SCS Software',
                'steam_id': '227300',
                'is_featured': True,
                'release_date': date(2012, 10, 19)
            },
            {
                'title': 'Cities: Skylines',
                'description': 'Современный симулятор города с глубокой системой управления.',
                'price': Decimal('799.00'),
                'points_price': 80,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/255710/header.jpg',
                'category': simulators,
                'developer': 'Colossal Order Ltd.',
                'publisher': 'Paradox Interactive',
                'steam_id': '255710',
                'is_featured': True,
                'release_date': date(2015, 3, 10)
            },
            
            # Дополнительные платформеры
            {
                'title': 'Celeste',
                'description': 'Сложная платформер-головоломка с отличной музыкой и историей.',
                'price': Decimal('399.00'),
                'points_price': 40,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/504230/header.jpg',
                'category': platformers,
                'developer': 'Maddy Makes Games',
                'publisher': 'Maddy Makes Games',
                'steam_id': '504230',
                'is_featured': True,
                'release_date': date(2018, 1, 25)
            },
            {
                'title': 'Ori and the Will of the Wisps',
                'description': 'Красивая платформер с атмосферной музыкой и эмоциональной историей.',
                'price': Decimal('999.00'),
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1057090/header.jpg',
                'category': platformers,
                'developer': 'Moon Studios',
                'publisher': 'Xbox Game Studios',
                'steam_id': '1057090',
                'is_featured': True,
                'release_date': date(2020, 3, 11)
            },
            
            # Дополнительные головоломки
            {
                'title': 'The Witness',
                'description': 'Загадочная головоломка на острове с множеством пазлов.',
                'price': Decimal('999.00'),
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/210970/header.jpg',
                'category': puzzle,
                'developer': 'Thekla, Inc.',
                'publisher': 'Thekla, Inc.',
                'steam_id': '210970',
                'is_featured': True,
                'release_date': date(2016, 1, 26)
            },
            {
                'title': 'Baba Is You',
                'description': 'Уникальная головоломка, где правила можно изменять.',
                'price': Decimal('299.00'),
                'points_price': 30,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/736260/header.jpg',
                'category': puzzle,
                'developer': 'Hempuli Oy',
                'publisher': 'Hempuli Oy',
                'steam_id': '736260',
                'is_featured': True,
                'release_date': date(2019, 3, 13)
            },
            
            # Дополнительные приключения
            {
                'title': 'God of War',
                'description': 'Эпическое приключение Кратоса и Атрея в мире скандинавской мифологии.',
                'price': Decimal('2999.00'),
                'points_price': 300,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1593500/header.jpg',
                'category': adventure,
                'developer': 'Santa Monica Studio',
                'publisher': 'Sony Interactive Entertainment',
                'steam_id': '1593500',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2022, 1, 14)
            },
            {
                'title': 'Horizon Zero Dawn',
                'description': 'Открытый мир с роботами-животными в постапокалиптическом будущем.',
                'price': Decimal('1999.00'),
                'points_price': 200,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1151640/header.jpg',
                'category': adventure,
                'developer': 'Guerrilla Games',
                'publisher': 'Sony Interactive Entertainment',
                'steam_id': '1151640',
                'is_featured': True,
                'release_date': date(2020, 8, 7)
            },
            
            # Дополнительные спортивные игры
            {
                'title': 'NBA 2K24',
                'description': 'Лучший баскетбольный симулятор с реалистичной физикой.',
                'price': Decimal('2999.00'),
                'points_price': 300,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/2338770/header.jpg',
                'category': sports,
                'developer': 'Visual Concepts',
                'publisher': '2K',
                'steam_id': '2338770',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2023, 9, 8)
            },
            {
                'title': 'Rocket League',
                'description': 'Футбол на автомобилях! Бесплатная игра с уникальным геймплеем.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/252950/header.jpg',
                'category': sports,
                'developer': 'Psyonix',
                'publisher': 'Psyonix',
                'steam_id': '252950',
                'is_featured': True,
                'release_date': date(2015, 7, 7)
            },
            
            # Дополнительные хорроры
            {
                'title': 'Dead by Daylight',
                'description': 'Асимметричный хоррор, где один игрок - убийца, а четверо - выжившие.',
                'price': Decimal('999.00'),
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/381210/header.jpg',
                'category': horror,
                'developer': 'Behaviour Interactive Inc.',
                'publisher': 'Behaviour Interactive Inc.',
                'steam_id': '381210',
                'is_featured': True,
                'release_date': date(2016, 6, 14)
            },
            {
                'title': 'Phasmophobia',
                'description': 'Кооперативный хоррор про охоту на призраков с друзьями.',
                'price': Decimal('399.00'),
                'points_price': 40,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/739630/header.jpg',
                'category': horror,
                'developer': 'Kinetic Games',
                'publisher': 'Kinetic Games',
                'steam_id': '739630',
                'is_featured': True,
                'release_date': date(2020, 9, 18)
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
