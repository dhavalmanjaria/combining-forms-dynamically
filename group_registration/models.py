from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.ForeignKey(User)
    GAME_CHOICES = (
                   ('CS', 'Counter-Strike'),
                   ('DOTA', 'DotA'),
                   ('LOL', 'League of Legends'))

    game = models.CharField(max_length=4, choices=GAME_CHOICES)
    team_name = models.CharField(max_length=100,
                                 help_text='Enter the name of your team')


class Spectator(models.Model):
    user = models.ForeignKey(User)
    TICKET_CHOICES = (
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Platinum'))

    ticket_class = models.CharField(max_length=2, choices=TICKET_CHOICES)

    coupon_code = models.CharField(max_length=5)


class BasicInfo(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20)