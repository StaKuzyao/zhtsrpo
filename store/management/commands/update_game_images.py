from django.core.management.base import BaseCommand
from store.models import Game


class Command(BaseCommand):
    help = 'Обновляет картинки для существующих игр'

    def handle(self, *args, **options):
        # Обновляем картинки для существующих игр
        games_to_update = {
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
        }

        for title, image_url in games_to_update.items():
            try:
                game = Game.objects.get(title=title)
                game.image_url = image_url
                game.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Обновлена картинка для: {game.title}')
                )
            except Game.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Игра не найдена: {title}')
                )
