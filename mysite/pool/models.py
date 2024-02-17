from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):
    player_1 = models.ForeignKey(Player, related_name='games_as_player_1', on_delete=models.CASCADE)
    player_2 = models.ForeignKey(Player, related_name='games_as_player_2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='won_games', on_delete=models.CASCADE)
    game_date = models.DateTimeField()

    def __str__(self):
        return f'{self.player_1.name} vs {self.player_2.name} - Winner: {self.winner.name}'
