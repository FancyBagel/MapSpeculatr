from celery import shared_task
from .models import User

@shared_task
def modify(record):
    u = User.objects.get(id=record['user'])
    if u.gamesPlayed == 0:
        u.averageScore = 0
    u.gamesPlayed += 1
    ratio = float(u.gamesPlayed - 1)/float(u.gamesPlayed)
    addition = float(record['score'])/float(u.gamesPlayed)
    u.averageScore = u.averageScore * ratio
    u.averageScore = u.averageScore + addition
    u.save()

    print(record)
    return