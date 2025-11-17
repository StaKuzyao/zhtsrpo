from django.contrib import admin
from .models import Question, Streak


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "category")


@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ("user", "current_streak")

# Register your models here.
