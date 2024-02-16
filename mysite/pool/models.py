from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    number_of_games = models.IntegerField(default=0)
    number_of_games_won = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    players = models.ManyToManyField(Player, related_name='games_played')
    winner = models.ForeignKey(Player, related_name='won_games', on_delete=models.CASCADE)
    game_date = models.DateTimeField()

    def __str__(self):
        return f"{self.players.all()[0]} vs {self.players.all()[1]} - Winner: {self.winner}"


