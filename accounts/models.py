from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    points = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.username

class SavedCard(models.Model):
    """Simplified saved card stub. Stores non-sensitive display data only."""
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='saved_cards')
    brand = models.CharField(max_length=20, blank=True)
    last4 = models.CharField(max_length=4)
    exp_month = models.PositiveIntegerField()
    exp_year = models.PositiveIntegerField()
    cardholder_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Сохраненная карта'
        verbose_name_plural = 'Сохраненные карты'
        ordering = ['-is_default', '-created_at']

    def __str__(self) -> str:
        return f"{self.brand} •••• {self.last4}"

# Create your models here.
