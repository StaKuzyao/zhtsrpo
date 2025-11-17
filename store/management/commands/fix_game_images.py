from django.core.management.base import BaseCommand
from store.models import Game


class Command(BaseCommand):
    help = 'Исправляет картинки для всех игр'

    def handle(self, *args, **options):
        # Словарь с правильными картинками для всех игр
        game_images = {
            'Counter-Strike 2': 'https://cdn.akamai.steamstatic.com/steam/apps/730/header.jpg',
            'Call of Duty: Modern Warfare III': 'https://cdn.akamai.steamstatic.com/steam/apps/2519060/header.jpg',
            'Apex Legends': 'https://cdn.akamai.steamstatic.com/steam/apps/1172470/header.jpg',
            'Age of Empires IV': 'https://cdn.akamai.steamstatic.com/steam/apps/1466860/header.jpg',
            'Civilization VI': 'https://cdn.akamai.steamstatic.com/steam/apps/289070/header.jpg',
            'The Witcher 3: Wild Hunt': 'https://cdn.akamai.steamstatic.com/steam/apps/292030/header.jpg',
            'Elden Ring': 'https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg',
            'Baldur\'s Gate 3': 'https://cdn.akamai.steamstatic.com/steam/apps/1086940/header.jpg',
            'Forza Horizon 5': 'https://cdn.akamai.steamstatic.com/steam/apps/1551360/header.jpg',
            'Microsoft Flight Simulator': 'https://cdn.akamai.steamstatic.com/steam/apps/1250410/header.jpg',
            'Hollow Knight': 'https://cdn.akamai.steamstatic.com/steam/apps/367520/header.jpg',
            'Portal 2': 'https://cdn.akamai.steamstatic.com/steam/apps/620/header.jpg',
            'The Last of Us Part I': 'https://cdn.akamai.steamstatic.com/steam/apps/1888930/header.jpg',
            'FIFA 24': 'https://cdn.akamai.steamstatic.com/steam/apps/2529500/header.jpg',
            'Resident Evil 4': 'https://cdn.akamai.steamstatic.com/steam/apps/2050650/header.jpg',
            'Valorant': 'https://cdn.akamai.steamstatic.com/steam/apps/1276090/header.jpg',
            'Overwatch 2': 'https://cdn.akamai.steamstatic.com/steam/apps/2357570/header.jpg',
            'Destiny 2': 'https://cdn.akamai.steamstatic.com/steam/apps/1085660/header.jpg',
            'Total War: Warhammer III': 'https://cdn.akamai.steamstatic.com/steam/apps/1142710/header.jpg',
            'Crusader Kings III': 'https://cdn.akamai.steamstatic.com/steam/apps/1158310/header.jpg',
            'Cyberpunk 2077': 'https://cdn.akamai.steamstatic.com/steam/apps/1091500/header.jpg',
            'Divinity: Original Sin 2': 'https://cdn.akamai.steamstatic.com/steam/apps/435150/header.jpg',
            'Gran Turismo 7': 'https://cdn.akamai.steamstatic.com/steam/apps/1446780/header.jpg',
            'Dirt Rally 2.0': 'https://cdn.akamai.steamstatic.com/steam/apps/690790/header.jpg',
            'Euro Truck Simulator 2': 'https://cdn.akamai.steamstatic.com/steam/apps/227300/header.jpg',
            'Cities: Skylines': 'https://cdn.akamai.steamstatic.com/steam/apps/255710/header.jpg',
            'Celeste': 'https://cdn.akamai.steamstatic.com/steam/apps/504230/header.jpg',
            'Ori and the Will of the Wisps': 'https://cdn.akamai.steamstatic.com/steam/apps/1057090/header.jpg',
            'The Witness': 'https://cdn.akamai.steamstatic.com/steam/apps/210970/header.jpg',
            'Baba Is You': 'https://cdn.akamai.steamstatic.com/steam/apps/736260/header.jpg',
            'God of War': 'https://cdn.akamai.steamstatic.com/steam/apps/1593500/header.jpg',
            'Horizon Zero Dawn': 'https://cdn.akamai.steamstatic.com/steam/apps/1151640/header.jpg',
            'NBA 2K24': 'https://cdn.akamai.steamstatic.com/steam/apps/2338770/header.jpg',
            'Rocket League': 'https://cdn.akamai.steamstatic.com/steam/apps/252950/header.jpg',
            'Dead by Daylight': 'https://cdn.akamai.steamstatic.com/steam/apps/381210/header.jpg',
            'Phasmophobia': 'https://cdn.akamai.steamstatic.com/steam/apps/739630/header.jpg',
        }

        updated_count = 0
        not_found_count = 0

        for title, image_url in game_images.items():
            try:
                game = Game.objects.get(title=title)
                game.image_url = image_url
                game.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Обновлена картинка: {game.title}')
                )
            except Game.DoesNotExist:
                not_found_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Игра не найдена: {title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nОбновлено картинок: {updated_count}')
        )
        if not_found_count > 0:
            self.stdout.write(
                self.style.WARNING(f'Игр не найдено: {not_found_count}')
            )
