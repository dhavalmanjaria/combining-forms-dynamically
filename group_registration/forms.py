from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
import logging
LOG = logging.getLogger('app')


class BasicInfoForm(UserCreationForm):
    choices = [(0, '--------'), (1, 'Spectator'), (2, 'Player')]
    user_type = forms.ChoiceField(choices=choices, initial=None)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.user_type = self.cleaned_data['user_type']
            
            if commit:
                user.save()

            return user

class PlayerForm(forms.Form):
    game = forms.ChoiceField(models.Player.GAME_CHOICES)
    team_name = forms.CharField(max_length=100)

    def save(self, user, commit=True):
        player = models.Player.objects.create(user=user)
        player.user = user
        player.game = self.cleaned_data['game']
        player.team_name = self.cleaned_data['team_name']

        if commit:
            player.save()

        return player


class SpectatorForm(forms.Form):
    ticket_class = forms.ChoiceField(models.Spectator.TICKET_CHOICES)
    coupon_code = forms.CharField(max_length=5)

    def save(self, user, commit=True):
        spectator = models.Spectator.objects.create(user=user)
        spectator.ticket_class = self.cleaned_data['ticket_class']
        spectator.coupon_code = self.cleaned_data['coupon_code']

        if commit:
            spectator.save()

        return spectator
