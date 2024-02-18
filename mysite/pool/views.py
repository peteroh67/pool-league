from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

def index(request):
    return render(request, "pool/index.html")

def add_game(request):
    return HttpResponse("Add a game of pool")

def league_table(request, start_date, end_date):
    return render(request, "pool/leaguetable.html")

def games(request):
    latest_games_list = Game.objects.order_by("game_date")[:20]
    context = {"latest_games_list": latest_games_list}
    return render(request, "pool/games.html", context)

def player(request, player_id):
    return HttpResponse(f"Viewing player {player_id}")

def players(request):
    return render(request, "pool/players.html")
