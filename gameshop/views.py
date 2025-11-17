from django.shortcuts import render
from store.models import Game, Category


def home(request):
    """Главная страница с акциями, скидками и категориями"""
    # Рекомендуемые игры (с флагом is_featured)
    featured_games = Game.objects.filter(is_featured=True)[:6]
    
    # Игры на распродаже
    sale_games = Game.objects.filter(is_on_sale=True)[:8]
    
    # Новые игры
    new_games = Game.objects.filter(is_new=True)[:8]
    
    # Все категории
    categories = Category.objects.all()[:8]
    
    context = {
        'featured_games': featured_games,
        'sale_games': sale_games,
        'new_games': new_games,
        'categories': categories,
    }
    
    return render(request, 'home.html', context)
