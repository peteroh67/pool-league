from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leaguetable/<int:month>/', views.league_table, name='league_table'),
    path('games/<int:month>/', views.games, name='games'),
    path('addgames/', views.add_games, name='add_games'),
    path('addplayers/', views.add_players, name='add_players')

]
