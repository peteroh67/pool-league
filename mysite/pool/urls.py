from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leaguetable/', views.leaguetable, name='leaguetable'),
    path('games/', views.games, name='games'),
    path('games/<int:month>/', views.games, name='games_by_month')
]
