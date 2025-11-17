from django.core.management.base import BaseCommand
from store.models import Game, Category
from decimal import Decimal
from datetime import date


class Command(BaseCommand):
    help = 'Добавляет популярные игры из Steam с описаниями'

    def handle(self, *args, **options):
        # Получаем категории
        try:
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
        except Category.DoesNotExist as e:
            self.stdout.write(
                self.style.ERROR(f'Категория не найдена: {e}')
            )
            return

        games = [
            # Шутеры
            {
                'title': 'Team Fortress 2',
                'description': 'Классический бесплатный шутер от Valve с уникальными классами персонажей. Сражайтесь в командах в различных игровых режимах с юмором и стилем. Одна из самых популярных игр в Steam.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/440/header.jpg',
                'category': shooters,
                'developer': 'Valve',
                'publisher': 'Valve',
                'steam_id': '440',
                'is_featured': True,
                'release_date': date(2007, 10, 10)
            },
            {
                'title': 'Left 4 Dead 2',
                'description': 'Кооперативный хоррор-шутер о выживании в зомби-апокалипсисе. Играйте с друзьями против орд зомби в эпических кампаниях. Классика жанра с отличным геймплеем.',
                'price': Decimal('299.00'),
                'points_price': 30,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/550/header.jpg',
                'category': shooters,
                'developer': 'Valve',
                'publisher': 'Valve',
                'steam_id': '550',
                'is_featured': True,
                'release_date': date(2009, 11, 17)
            },
            
            # Стратегии
            {
                'title': 'Stellaris',
                'description': 'Грандиозная космическая стратегия 4X от Paradox Interactive. Создайте свою галактическую империю, исследуйте новые миры, встречайте инопланетные цивилизации и управляйте судьбой галактики.',
                'price': Decimal('999.00'),
                'original_price': Decimal('1299.00'),
                'discount_percent': 23,
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/281990/header.jpg',
                'category': strategy,
                'developer': 'Paradox Development Studio',
                'publisher': 'Paradox Interactive',
                'steam_id': '281990',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2016, 5, 9)
            },
            
            # RPG
            {
                'title': 'Fallout: New Vegas',
                'description': 'Культовая RPG в постапокалиптическом мире. Исследуйте пустоши Лас-Вегаса, принимайте важные решения и формируйте судьбу пустошей. Одна из лучших RPG всех времен.',
                'price': Decimal('499.00'),
                'points_price': 50,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/22380/header.jpg',
                'category': rpg,
                'developer': 'Obsidian Entertainment',
                'publisher': 'Bethesda Softworks',
                'steam_id': '22380',
                'is_featured': True,
                'release_date': date(2010, 10, 19)
            },
            
            # Гонки
            {
                'title': 'Need for Speed: Heat',
                'description': 'Современные уличные гонки в Майами. Соревнуйтесь днем и ночью, настраивайте автомобили и избегайте полиции в этой захватывающей аркаде от EA.',
                'price': Decimal('1999.00'),
                'original_price': Decimal('2499.00'),
                'discount_percent': 20,
                'points_price': 200,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1222680/header.jpg',
                'category': racing,
                'developer': 'Ghost Games',
                'publisher': 'Electronic Arts',
                'steam_id': '1222680',
                'is_on_sale': True,
                'is_featured': True,
                'release_date': date(2019, 11, 8)
            },
            
            # Симуляторы
            {
                'title': 'The Sims 4',
                'description': 'Создавайте и управляйте жизнью ваших симов в этой популярной симуляции жизни. Стройте дома, развивайте карьеру, заводите семьи и живите виртуальной жизнью мечты.',
                'price': Decimal('0.00'),
                'points_price': 0,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1222670/header.jpg',
                'category': simulators,
                'developer': 'Maxis',
                'publisher': 'Electronic Arts',
                'steam_id': '1222670',
                'is_featured': True,
                'is_new': True,
                'release_date': date(2014, 9, 2)
            },
            
            # Платформеры
            {
                'title': 'Cuphead',
                'description': 'Сложный платформер в стиле 1930-х мультфильмов. Сражайтесь с боссами, преодолевайте препятствия и наслаждайтесь потрясающей анимацией в стиле ретро.',
                'price': Decimal('799.00'),
                'points_price': 80,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/268910/header.jpg',
                'category': platformers,
                'developer': 'Studio MDHR',
                'publisher': 'Studio MDHR',
                'steam_id': '268910',
                'is_featured': True,
                'release_date': date(2017, 9, 29)
            },
            
            # Головоломки
            {
                'title': 'Tetris Effect',
                'description': 'Современная версия классического Тетриса с потрясающими визуальными эффектами и музыкой. Погрузитесь в медитативный опыт игры в Тетрис с новым уровнем красоты.',
                'price': Decimal('999.00'),
                'points_price': 100,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1003590/header.jpg',
                'category': puzzle,
                'developer': 'Monstars Inc.',
                'publisher': 'Enhance Games',
                'steam_id': '1003590',
                'is_featured': True,
                'release_date': date(2019, 7, 23)
            },
            
            # Приключения
            {
                'title': 'Life is Strange',
                'description': 'Эмоциональная приключенческая игра о подростке Макс, которая обнаруживает способность перематывать время. Принимайте важные решения и влияйте на судьбу персонажей.',
                'price': Decimal('399.00'),
                'points_price': 40,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/319630/header.jpg',
                'category': adventure,
                'developer': 'Dontnod Entertainment',
                'publisher': 'Square Enix',
                'steam_id': '319630',
                'is_featured': True,
                'release_date': date(2015, 1, 30)
            },
            
            # Хоррор
            {
                'title': 'Outlast',
                'description': 'Ужасающий хоррор от первого лица в психиатрической больнице. Выживайте, используя только камеру с ночным видением, и избегайте ужасных обитателей больницы.',
                'price': Decimal('399.00'),
                'points_price': 40,
                'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/238320/header.jpg',
                'category': horror,
                'developer': 'Red Barrels',
                'publisher': 'Red Barrels',
                'steam_id': '238320',
                'is_featured': True,
                'release_date': date(2013, 9, 4)
            }
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
