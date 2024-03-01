# Import Django's settings module and configure it
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

# Import necessary modules
import random
from datetime import datetime, timedelta
from django.utils import timezone
from pool.models import Player, Game

# Get all players from the database
players = Player.objects.all()

# Generate random game data for the last 3 months
start_date = timezone.now() - timedelta(days=90)  # Start date is 3 months ago
end_date = timezone.now()  # End date is today

current_date = start_date
while current_date <= end_date:
    # Generate 5 random games for each day
    for i in range(5):
        # Choose random players for player 1 and player 2
        player_1 = random.choice(players)
        player_2 = random.choice(players)

        # Ensure player 1 and player 2 are not the same
        while player_1 == player_2:
            player_2 = random.choice(players)

        # Choose a random winner from player 1 and player 2
        winner = random.choice([player_1, player_2])

        # Create a new game instance and save it to the database
        game = Game.objects.create(
            player_1=player_1,
            player_2=player_2,
            winner=winner,
            game_date=current_date
        )

    # Move to the next day
    current_date += timedelta(days=1)
