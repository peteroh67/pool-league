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
    class Meta:
        model = Game
        fields = "__all__"

