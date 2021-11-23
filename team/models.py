from django.db import models
from django.db.models.deletion import PROTECT
from django.urls import reverse
import uuid
class Team(models.Model):
    team_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="team")
    description = models.CharField(verbose_name="Team Descriptions", max_length=255, default="")
    slug = models.SlugField(null=False, unique=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, unique=True)

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.id)])

class Member(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=True, default="")
    team = models.ForeignKey(Team, verbose_name="Team", on_delete=PROTECT)
    avatar = models.ImageField(upload_to="member")
    description =models.CharField(max_length=255, default="")
    slug = models.SlugField(null=False, unique=True, default="")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member_detail', args=[str(self.name)])