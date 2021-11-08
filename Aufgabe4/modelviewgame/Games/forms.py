from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['name', 'description', 'studio', 'release_published', 'genre', 'fsk']
        widgets = {
            'genre': forms.Select(choices=Game.GENRE),
            'fsk': forms.Select(choices=Game.FSK),
            'user': forms.HiddenInput(),
        }
