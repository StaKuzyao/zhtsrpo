from django.core.management.base import BaseCommand
from store.models import Game
from decimal import Decimal


class Command(BaseCommand):
    help = 'Убеждается что FIFA 24 в акциях'

    def handle(self, *args, **options):
        try:
            fifa = Game.objects.get(title='FIFA 24')
            
            # Устанавливаем все параметры для акции
            fifa.is_on_sale = True
            fifa.is_featured = True
            fifa.is_new = True
            fifa.discount_percent = 25
            fifa.original_price = Decimal('3999.00')
            fifa.price = Decimal('2999.00')
            fifa.points_price = 300
            fifa.image_url = 'https://cdn.akamai.steamstatic.com/steam/apps/2529500/header.jpg'
            fifa.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'FIFA 24 настроена для акций:')
            )
            self.stdout.write(f'  - Скидка: {fifa.discount_percent}%')
            self.stdout.write(f'  - Оригинальная цена: {fifa.original_price} руб')
            self.stdout.write(f'  - Цена со скидкой: {fifa.price} руб')
            self.stdout.write(f'  - На распродаже: {fifa.is_on_sale}')
            self.stdout.write(f'  - Рекомендуемая: {fifa.is_featured}')
            self.stdout.write(f'  - Новинка: {fifa.is_new}')
            self.stdout.write(f'  - Картинка: {fifa.image_url[:50]}...')
            
        except Game.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('FIFA 24 не найдена в базе данных')
            )
