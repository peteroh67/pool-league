from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leaguetable/<int:month>/', views.leaguetable, name='league_table'),
    path('games/<int:month>/', views.games, name='games'),
    path('addgames/', views.games, name='add_games'),
    path('addplayers/', views.games, name='add_players')

]
