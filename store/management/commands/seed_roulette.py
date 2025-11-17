from django.core.management.base import BaseCommand
from store.models import RouletteGame, Game


class Command(BaseCommand):
    help = 'Создает тестовые данные для рулетки'

    def handle(self, *args, **options):
        # Создаем игры рулетки
        roulette_games = [
            {
                'name': 'Классическая рулетка',
                'description': 'Попробуйте удачу в классической рулетке!',
                'price': 50.00,
                'probability': 0.3,  # 30% шанс выиграть
                'is_active': True,
            },
            {
                'name': 'Золотая рулетка',
                'description': 'Премиум рулетка с повышенными шансами!',
                'price': 100.00,
                'probability': 0.5,  # 50% шанс выиграть
                'is_active': True,
            },
            {
                'name': 'Эксклюзивная рулетка',
                'description': 'Самая дорогая рулетка с лучшими призами!',
                'price': 200.00,
                'probability': 0.7,  # 70% шанс выиграть
                'is_active': True,
            },
        ]

        for idx, game_data in enumerate(roulette_games):
            rg, created = RouletteGame.objects.get_or_create(
                name=game_data['name'],
                defaults=game_data
            )
            # Присваиваем пул призов: разные срезы списка игр
            all_games = list(Game.objects.all())
            if all_games:
                if idx == 0:
                    prizes = all_games[:6]
                elif idx == 1:
                    prizes = all_games[6:12] if len(all_games) > 12 else all_games[:6]
                else:
                    prizes = all_games[12:18] if len(all_games) > 18 else all_games[-6:]
                rg.prizes.set(prizes)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создана рулетка: {rg.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Рулетка уже существует: {rg.name}'))

        self.stdout.write(
            self.style.SUCCESS('Тестовые данные рулетки созданы успешно!')
        )
