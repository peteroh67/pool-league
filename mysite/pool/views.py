from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from datetime import datetime

def index(request):
    return render(request, "pool/index.html")

def add_game(request):
    return HttpResponse("Add a game of pool")

def leaguetable(request, month=None):
    return render(request, "pool/leaguetable.html")

# Returns a view of all games in a specified month. Returns all games in the current month by default
def games(request, month=None):
    if month is None:
        month = datetime.now().month

    games_in_month = Game.objects.filter(game_date__month=month).order_by("game_date")
    context = {"latest_games_list": games_in_month}

    return render(request, "pool/games.html", context)
