from django.db import models
from django.conf import settings


class Question(models.Model):
    text = models.TextField()
    correct_answer = models.CharField(max_length=200)
    incorrect_answers = models.JSONField(default=list, blank=True)
    category = models.CharField(max_length=100, default='IT')

    def __str__(self) -> str:
        return self.text[:60]


class Streak(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_streak = models.PositiveIntegerField(default=0)

    def increment(self) -> int:
        self.current_streak += 1
        self.save(update_fields=["current_streak"])
        return self.current_streak

    def reset(self) -> None:
        self.current_streak = 0
        self.save(update_fields=["current_streak"])

# Create your models here.
