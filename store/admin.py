from django.contrib import admin
from .models import Game, Purchase, Category, RouletteGame, RouletteSpin, RouletteAttempt


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "discount_percent", "is_on_sale", "is_featured", "is_new")
    list_filter = ("category", "is_on_sale", "is_featured", "is_new", "created_at")
    search_fields = ("title", "developer", "publisher")
    list_editable = ("is_on_sale", "is_featured", "is_new", "discount_percent")
    fieldsets = (
        ("Основная информация", {
            "fields": ("title", "description", "category", "image_url")
        }),
        ("Цены", {
            "fields": ("price", "original_price", "discount_percent", "points_price")
        }),
        ("Статусы", {
            "fields": ("is_on_sale", "is_featured", "is_new")
        }),
        ("Дополнительная информация", {
            "fields": ("developer", "publisher", "release_date", "steam_id"),
            "classes": ("collapse",)
        })
    )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "game", "payment_method", "used_points", "created_at")
    list_filter = ("payment_method", "used_points", "created_at")
    search_fields = ("user__username", "game__title")


@admin.register(RouletteGame)
class RouletteGameAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "probability", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    list_editable = ("is_active",)


@admin.register(RouletteSpin)
class RouletteSpinAdmin(admin.ModelAdmin):
    list_display = ("user", "game", "won_game", "cost", "created_at")
    list_filter = ("created_at", "game")
    search_fields = ("user__username", "game__name", "won_game__title")


@admin.register(RouletteAttempt)
class RouletteAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "attempts_used", "max_attempts")
    list_filter = ("date",)
    search_fields = ("user__username",)

# Register your models here.
