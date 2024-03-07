from django import forms
from .models import Player

class PlayerForm(forms.Form):
    class meta:
        player_name = forms.CharField(label="Player name", max_length=100)
