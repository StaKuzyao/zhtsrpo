from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
import random
from .models import Game, Purchase, Category, RouletteGame, RouletteSpin, RouletteAttempt


class GameListView(View):
    def get(self, request):
        games = Game.objects.all()
        categories = Category.objects.all()
        
        # Фильтрация по категории
        category_slug = request.GET.get('category')
        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug)
                games = games.filter(category=category)
            except Category.DoesNotExist:
                pass
        
        # Фильтрация по статусу
        status = request.GET.get('status')
        if status == 'sale':
            games = games.filter(is_on_sale=True)
        elif status == 'new':
            games = games.filter(is_new=True)
        elif status == 'featured':
            games = games.filter(is_featured=True)
        
        owned_ids = set(Purchase.objects.filter(user=request.user).values_list('game_id', flat=True)) if request.user.is_authenticated else set()
        
        context = {
            'games': games,
            'owned_ids': owned_ids,
            'categories': categories,
            'current_category': category_slug,
            'current_status': status,
        }
        return render(request, 'store/game_list.html', context)


class GameDetailView(View):
    def get(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        owned = request.user.is_authenticated and Purchase.objects.filter(user=request.user, game=game).exists()
        return render(request, 'store/game_detail.html', {'game': game, 'owned': owned})


@login_required
@transaction.atomic
def buy_with_card(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if Purchase.objects.filter(user=request.user, game=game).exists():
        return redirect('store:detail', pk=pk)
    
    # Заглушка для оплаты картой - просто создаем покупку
    card_number = request.POST.get('card_number', '**** **** **** 1234')
    card_holder = request.POST.get('card_holder', 'Иван Иванов')
    
    Purchase.objects.create(
        user=request.user, 
        game=game, 
        used_points=False,
        payment_method='card',
        card_number=card_number,
        card_holder=card_holder
    )
    messages.success(request, f'Игра "{game.title}" успешно куплена!')
    return redirect('store:detail', pk=pk)


@login_required
@transaction.atomic
def buy_with_points(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if Purchase.objects.filter(user=request.user, game=game).exists():
        return redirect('store:detail', pk=pk)
    if game.points_price and request.user.points >= game.points_price:
        request.user.points -= game.points_price
        request.user.save(update_fields=['points'])
        Purchase.objects.create(
            user=request.user, 
            game=game, 
            used_points=True,
            payment_method='points'
        )
        messages.success(request, f'Игра "{game.title}" куплена за очки!')
    return redirect('store:detail', pk=pk)


class RouletteView(View):
    def get(self, request):
        roulette_games = RouletteGame.objects.filter(is_active=True)
        today = timezone.now().date()
        
        # Получаем или создаем запись о попытках на сегодня
        attempt, created = RouletteAttempt.objects.get_or_create(
            user=request.user,
            date=today,
            defaults={'attempts_used': 0}
        )
        
        # Для первой рулетки показываем ее пул призов (или пусто)
        first = roulette_games.first()
        available_games = first.prizes.all()[:12] if first else Game.objects.none()
        
        context = {
            'roulette_games': roulette_games,
            'attempt': attempt,
            'available_games': available_games,
        }
        return render(request, 'store/roulette.html', context)


@login_required
@transaction.atomic
def spin_roulette(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)
    
    roulette_game_id = request.POST.get('roulette_game_id')
    if not roulette_game_id:
        return JsonResponse({'error': 'Не выбрана игра рулетки'}, status=400)
    
    roulette_game = get_object_or_404(RouletteGame, id=roulette_game_id, is_active=True)
    today = timezone.now().date()
    
    # Проверяем попытки
    attempt, created = RouletteAttempt.objects.get_or_create(
        user=request.user,
        date=today,
        defaults={'attempts_used': 0}
    )
    
    if not attempt.can_spin():
        return JsonResponse({'error': 'Превышено количество попыток на сегодня'}, status=400)
    
    # Проверяем баланс
    if request.user.balance < roulette_game.price:
        return JsonResponse({'error': 'Недостаточно средств'}, status=400)
    
    # Списываем стоимость
    request.user.balance -= roulette_game.price
    request.user.save(update_fields=['balance'])
    
    # Увеличиваем количество попыток
    attempt.attempts_used += 1
    attempt.save(update_fields=['attempts_used'])
    
    # Определяем выигрыш (беспроигрышная): выбираем случайную игру из пула рулетки
    prize_qs = roulette_game.prizes.all()
    won_game = None
    if prize_qs.exists():
        won_game = random.choice(list(prize_qs))
        # Добавляем игру в библиотеку пользователя, если еще нет
        Purchase.objects.get_or_create(
            user=request.user,
            game=won_game,
            defaults={
                'used_points': False,
                'payment_method': 'card',
                'card_number': 'РУЛЕТКА',
                'card_holder': 'Выигрыш'
            }
        )
    
    # Создаем запись о вращении
    spin = RouletteSpin.objects.create(
        user=request.user,
        game=roulette_game,
        won_game=won_game,
        cost=roulette_game.price
    )
    
    return JsonResponse({
        'success': True,
        'won_game': {
            'id': won_game.id,
            'title': won_game.title,
            'image_url': won_game.image_url,
        } if won_game else None,
        'attempts_remaining': attempt.attempts_remaining,
        'new_balance': float(request.user.balance),
    })

# Create your views here.
