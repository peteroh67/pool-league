from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Player
from datetime import datetime

def index(request):
    current_month = datetime.now().strftime('%m')

    games_url = f'games/{current_month}/'
    league_url = f'leaguetable/{current_month}'

    context = {
        'games_url': games_url,
        'league_url': league_url
        }

    return render(request, "pool/index.html", context)

def leaguetable(request, month=None):
    if month is None:
        month = datetime.now().month

    games_in_month = Game.objects.filter(game_date__month=month).order_by("game_date")
    players = Player.objects.all()

    context = {}

    for player in players:
        stats = get_player_stats(player, games_in_month)
        context[player] = stats

    return render(request, "pool/leaguetable.html", context)

# return player stats where [0] == games played, [1] == wins
def get_player_stats(player, games):
    playerStats = [0, 0, 0]

    for game in games:
        if game.player_1 == player or game.player_2 == player:
            playerStats[0] += 1

            if game.winner == player:
                playerStats[1] += 1

    return playerStats


# Returns a view of all games in a specified month. Returns all games in the current month by default
def games(request, month=None):
    if month is None:
        month = datetime.now().month

    games_in_month = Game.objects.filter(game_date__month=month).order_by("-game_date")
    players = Player.objects.all()
    context = {
        "games_list": games_in_month,
        "players": players
        }

    return render(request, "pool/games.html", context)

def add_game(request):
    return HttpResponse("Add a game of pool")

def add_player(request):
    return HttpResponse("Add a pool player")

