from celery import shared_task
from .models import Stat, Map

@shared_task
def add(record):
    m = Map.objects.get(id=record['map'])
    if Stat.objects.filter(map=m, user_id=record['id']).count == 0:
        s = Stat(map=m, user_id=record['id'], highscore=record['result'])
        s.save()
    else:
        s = Stat.objects.get(map=m, user_id=record['id'])
        s.highscore = min(s.highscore, record['result'])
        s.save()
    print(record)
    return
