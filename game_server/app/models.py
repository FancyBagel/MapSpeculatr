from django.db import models

# Create your models here.

class Game(models.Model):
    player = models.IntegerField(primary_key=True)
    map = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    points = models.IntegerField()
    current = models.IntegerField()
