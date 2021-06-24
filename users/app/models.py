from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    password = models.CharField(max_length = 30)
    joinDate = models.DateField()
    gamesPlayed = models.IntegerField(default=0)
    averageScore = models.FloatField(null=True)
