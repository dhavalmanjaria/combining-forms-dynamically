from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_basic_info(sender, instance, created, **kwargs):
    if created:
        BasicInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_basic_info(sender, instance, **kwargs):
    instance.basicinfo.save()
