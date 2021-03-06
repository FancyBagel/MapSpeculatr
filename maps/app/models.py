from django.db import models

# Create your models here.

class Map(models.Model):
    name = models.CharField(max_length=200)

class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    map = models.ForeignKey('Map', on_delete=models.CASCADE)

class Stat(models.Model):
    map = models.ForeignKey('Map', on_delete=models.CASCADE)
    user_id = models.IntegerField()
    highscore = models.IntegerField()
    