from celery import shared_task
from .models import Stat, Map

@shared_task
def add(record):
    m = Map.objects.get(id=record['map'])

    s = Stat(map=m, user_id=record['id'], highscore=record['result'])
    s.save()

    print(record)
    return
