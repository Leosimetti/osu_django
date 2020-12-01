from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True, default="")
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    hours_played = models.FloatField(default=0.0, blank=False)
    successful_map_plays = models.IntegerField(default=0, blank=False)
    map_plays = models.IntegerField(default=0, blank=False)
    total_score = models.IntegerField(default=0, blank=False)
    friends = models.ManyToManyField('self', symmetrical=False, blank=True)
    profile_picture_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

class mapPlay(models.Model):
    user  = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    date  = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    mapid = models.IntegerField(blank=False, default=228)