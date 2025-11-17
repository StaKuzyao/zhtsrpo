from django.urls import path
from .views import GameListView, GameDetailView, buy_with_card, buy_with_points, RouletteView, spin_roulette

app_name = 'store'

urlpatterns = [
    path('', GameListView.as_view(), name='list'),
    path('<int:pk>/', GameDetailView.as_view(), name='detail'),
    path('<int:pk>/buy/card/', buy_with_card, name='buy_card'),
    path('<int:pk>/buy/points/', buy_with_points, name='buy_points'),
    path('roulette/', RouletteView.as_view(), name='roulette'),
    path('roulette/spin/', spin_roulette, name='spin_roulette'),
]


