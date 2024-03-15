from django import forms
from .models import Player, Game

class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["name"]

    def clean_name(self):
        name = self.cleaned_data['name']

        if Player.objects.filter(name=name).exists():
            raise forms.ValidationError("This player name already exists.")
        return name

class NewGameForm(forms.ModelForm):
    winner = forms.ChoiceField(choices=(('player_1', 'Player 1'), ('player_2', 'Player 2')), widget=forms.RadioSelect, required=True)
    class Meta:
        model = Game
        fields = ['player_1', 'player_2'] # game will be preprocessed in the view to get current datetime and set winner from radio
        widgets = {
            'player_1': forms.Select(attrs={'class': 'button'}),
            'player_2': forms.Select(attrs={'class': 'button'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        player_1 = cleaned_data.get('player_1')
        player_2 = cleaned_data.get('player_2')

        if player_1 == player_2:
            raise forms.ValidationError("Player 1 and Player 2 cannot be the same.")

        return cleaned_data


