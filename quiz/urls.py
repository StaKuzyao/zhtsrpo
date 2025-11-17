from django.urls import path
from .views import play

app_name = 'quiz'

urlpatterns = [
    path('play/', play, name='play'),
]


