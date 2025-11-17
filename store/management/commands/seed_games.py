from django.core.management.base import BaseCommand
from store.models import Game


class Command(BaseCommand):
    help = "Seed the database with curated real games and images"

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true", help="Delete all existing games before seeding")

    def handle(self, *args, **options):
        if options.get("reset"):
            deleted, _ = Game.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Deleted existing games: {deleted}"))

        # Общеизвестные игры с устойчивыми обложками (Wikipedia/Wikimedia)
        games = [
            {"title": "The Witcher 3: Wild Hunt", "description": "RPG в открытом мире.", "price": 899.00, "points_price": 90, "image_url": "https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg"},
            {"title": "Grand Theft Auto V", "description": "Экшен в открытом мире.", "price": 999.00, "points_price": 100, "image_url": "https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png"},
            {"title": "Minecraft", "description": "Песочница про строительство и выживание.", "price": 699.00, "points_price": 70, "image_url": "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png"},
            {"title": "Hades", "description": "Рогалик про побег из Аида.", "price": 499.00, "points_price": 50, "image_url": "https://upload.wikimedia.org/wikipedia/en/1/1a/Hades_cover_art.jpg"},
            {"title": "Celeste", "description": "Платформер о преодолении.", "price": 299.00, "points_price": 30, "image_url": "https://upload.wikimedia.org/wikipedia/en/9/9a/Celeste_box_art_full.png"},
            {"title": "Cyberpunk 2077", "description": "RPG в Найт-Сити.", "price": 1099.00, "points_price": 110, "image_url": "https://upload.wikimedia.org/wikipedia/en/9/9f/Cyberpunk_2077_box_art.jpg"},
            {"title": "Red Dead Redemption 2", "description": "Запад, открытый мир.", "price": 1099.00, "points_price": 110, "image_url": "https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg"},
            {"title": "Elden Ring", "description": "Souls-like в открытом мире.", "price": 1099.00, "points_price": 110, "image_url": "https://upload.wikimedia.org/wikipedia/en/b/b9/Elden_Ring_Box_art.jpg"},
            {"title": "Stardew Valley", "description": "Фермерский симулятор.", "price": 399.00, "points_price": 40, "image_url": "https://upload.wikimedia.org/wikipedia/en/f/fd/Stardew_Valley_logo.jpg"},
            {"title": "Terraria", "description": "Песочница 2D с выживанием.", "price": 249.00, "points_price": 25, "image_url": "https://upload.wikimedia.org/wikipedia/en/9/9b/Terraria_Steam_artwork.jpg"},
        ]

        created = 0
        for g in games:
            obj, was_created = Game.objects.get_or_create(title=g["title"], defaults=g)
            if was_created:
                created += 1
            else:
                # Обновляем описание/цену/картинку, если уже существовало
                updated = False
                for key in ("description", "price", "points_price", "image_url"):
                    if getattr(obj, key) != g[key]:
                        setattr(obj, key, g[key])
                        updated = True
                if updated:
                    obj.save()
        self.stdout.write(self.style.SUCCESS(f"Games seeded. New: {created}, total: {Game.objects.count()}"))


