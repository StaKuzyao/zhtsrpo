from django.core.management.base import BaseCommand
from store.models import Game


class Command(BaseCommand):
    help = 'Обновляет FIFA 24 для акций'

    def handle(self, *args, **options):
        try:
            fifa = Game.objects.get(title='FIFA 24')
            fifa.is_on_sale = True
            fifa.is_featured = True
            fifa.discount_percent = 25
            fifa.original_price = 3999.00
            fifa.price = 2999.00
            fifa.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'FIFA 24 обновлена для акций: скидка {fifa.discount_percent}%')
            )
        except Game.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('FIFA 24 не найдена в базе данных')
            )
