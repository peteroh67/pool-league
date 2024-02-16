from django.db import models
from django.utils import timezone

class Player(models.Model):
    name = models.CharField(max_length=200)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
class Game(models.Model):
    player_1 = models.ForeignKey(Player, related_name='games_as_player_1', on_delete=models.CASCADE)
    player_2 = models.ForeignKey(Player, related_name='games_as_player_2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='won_games', on_delete=models.CASCADE)
    game_date = timezone.now().date()


