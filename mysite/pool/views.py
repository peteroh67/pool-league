from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Game, Player
from datetime import datetime
import calendar
from .forms import NewPlayerForm, NewGameForm

def index(request):
    current_month = timezone.now().strftime('%m')

    games_url = f'games/{current_month}/'
    league_url = f'leaguetable/{current_month}'

    context = {
        'games_url': games_url,
        'league_url': league_url
        }

    return render(request, "pool/index.html", context)

def league_table(request, month):

    games_in_month = Game.objects.filter(game_date__month=month)
    players = Player.objects.all()

    player_stats = [get_player_stats(player, games_in_month) for player in players]

    # Sort by win rate with the highest at the top of the table
    player_stats = sorted(player_stats, key=lambda x: x[3], reverse=True)

    context = {
        "month_str": calendar.month_name[month],
        "players_stats": player_stats
    }

    return render(request, "pool/leaguetable.html", context)

def get_player_stats(player, games):
    total_games = sum(1 for game in games if player in [game.player_1, game.player_2])
    wins = sum(1 for game in games if game.winner == player)

    win_rate = (wins / total_games) * 100 if total_games > 0 else 0
    win_rate = round(win_rate)

    return [player.name, total_games, wins, win_rate]


# Returns a view of all games in a specified month.
def games(request, month=None):

    games_in_month = Game.objects.filter(game_date__month=month).order_by("-game_date")
    players = Player.objects.all()

    return render(request, "pool/games.html", {"games_list": games_in_month, "players": players})

def add_players(request):

    if request.method == "POST":
        form = NewPlayerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_players')
    else:
        form = NewPlayerForm()

    players = Player.objects.all()

    return render(request,"pool/addplayers.html", {"players": players, "form": form})

def add_games(request):

    if request.method == 'POST':
        form = NewGameForm(request.POST)

        if form.is_valid():
            player_1 = form.cleaned_data['player_1']
            player_2 = form.cleaned_data['player_2']
            winner_rad = form.cleaned_data['winner']

            if winner_rad == 'player_1':
                winner = player_1
            else:
                winner = player_2

            game = Game(player_1=player_1, player_2=player_2, winner=winner, game_date=timezone.now())
            game.save()

            return redirect('add_games')

    else:
        form = NewGameForm()

    last_ten_games = Game.objects.order_by('-game_date')[:10]
    players = Player.objects.all()

    context = {
        'form': form,
        'players': players,
        'last_ten_games': last_ten_games
    }

    return render(request, 'pool/addgames.html', context)