from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('league_table/', views.league_table, name='league_table'),
    path('games/', views.games, name='games'),
    path('players/', views.players, name='players'),
    path('<int:player_id>/player/', views.player, name='player')
]
