from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    points_price = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True, default="")
    
    # Новые поля для акций и скидок
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Оригинальная цена до скидки")
    discount_percent = models.PositiveIntegerField(default=0, help_text="Процент скидки (0-100)")
    is_on_sale = models.BooleanField(default=False, help_text="Игра на распродаже")
    is_featured = models.BooleanField(default=False, help_text="Рекомендуемая игра")
    is_new = models.BooleanField(default=False, help_text="Новая игра")
    
    # Категория
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Дополнительные поля
    release_date = models.DateField(null=True, blank=True)
    developer = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    steam_id = models.CharField(max_length=50, blank=True, help_text="ID игры в Steam")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
    
    @property
    def discounted_price(self):
        """Возвращает цену со скидкой"""
        if self.discount_percent > 0:
            from decimal import Decimal
            discount_factor = Decimal('1') - Decimal(str(self.discount_percent)) / Decimal('100')
            return self.price * discount_factor
        return self.price
    
    @property
    def savings_amount(self):
        """Возвращает сумму экономии"""
        if self.original_price and self.discount_percent > 0:
            return self.original_price - self.discounted_price
        return 0


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    used_points = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=20, default='card', choices=[
        ('card', 'Банковская карта'),
        ('points', 'Очки'),
    ])
    card_number = models.CharField(max_length=19, blank=True, help_text="Номер карты (заглушка)")
    card_holder = models.CharField(max_length=100, blank=True, help_text="Владелец карты (заглушка)")

    class Meta:
        unique_together = ("user", "game")


class RouletteGame(models.Model):
    """Игра в рулетке"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Стоимость одного вращения")
    probability = models.FloatField(default=1.0, help_text="Вероятность выпадения (0.0-1.0)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    prizes = models.ManyToManyField('store.Game', related_name='available_in_roulettes', blank=True, help_text="Игры, которые выпадают в этой рулетке")

    class Meta:
        verbose_name = "Игра рулетки"
        verbose_name_plural = "Игры рулетки"

    def __str__(self):
        return self.name


class RouletteSpin(models.Model):
    """Запись о вращении рулетки пользователем"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(RouletteGame, on_delete=models.CASCADE)
    won_game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True, help_text="Выигранная игра")
    created_at = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Вращение рулетки"
        verbose_name_plural = "Вращения рулетки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.created_at}"


class RouletteAttempt(models.Model):
    """Отслеживание попыток пользователя в рулетке"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    attempts_used = models.PositiveIntegerField(default=0)
    max_attempts = models.PositiveIntegerField(default=5)

    class Meta:
        unique_together = ("user", "date")
        verbose_name = "Попытка рулетки"
        verbose_name_plural = "Попытки рулетки"

    def __str__(self):
        return f"{self.user.username} - {self.date} ({self.attempts_used}/{self.max_attempts})"

    @property
    def attempts_remaining(self):
        return max(0, self.max_attempts - self.attempts_used)

    def can_spin(self):
        return self.attempts_remaining > 0

# Create your models here.
