from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg, Sum
from api.get_username import *
from django.urls import reverse
import uuid
#Team Models
class TeamModel(models.Model):
    team_name = models.CharField(verbose_name="Team", max_length=200)
    # logo = models.ImageField(upload_to="teams")
    logo = models.URLField(verbose_name="Team Logo", max_length=200)
    def __str__(self):
        return self.team_name


#Upcoming Matches Models
class UpcomingMatche(models.Model):
    team_1 = models.ForeignKey(TeamModel,verbose_name="Team 1",related_name='%(class)s_requests_created', max_length=100, on_delete=PROTECT)
    team_2 = models.ForeignKey(TeamModel,verbose_name="Team 2", max_length=100, on_delete=PROTECT)
    date_tournament = models.DateTimeField(verbose_name="Date of Match")

    def __str__(self):
        return f"{self.team_1} vs {self.team_2}"

#Betting System Models
class BetModel(models.Model):
    BET_STATUS = (
        ('Win', 'Win'),
        ('Lose', 'Lose'),
        ('Ongoing', 'Ongoing'),
    )
    better = models.ForeignKey(User, verbose_name="Better", on_delete=PROTECT)
    matches = models.ForeignKey(UpcomingMatche, verbose_name="Matches", on_delete=PROTECT, default="", null=False, blank=False)
    pick = models.ForeignKey(TeamModel,verbose_name="Picked Team", on_delete=PROTECT, default="", null=False, blank=False)
    amount = models.IntegerField(verbose_name="Bet Amount", validators=[MinValueValidator(50), MaxValueValidator(1000)])
    status = models.CharField(max_length=10,verbose_name="Bet Status", default="", choices=BET_STATUS, blank=True, null=True)
    time = models.DateTimeField(verbose_name="Time of Bet", auto_now_add=True)

    def __str__(self):
        return f"{self.better} - {self.pick} - {self.matches} - {self.amount}"

    #get metches id
    def get_matches_id(self):
        return self.matches.id