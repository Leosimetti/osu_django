from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
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
