# Generated by Django 3.1.3 on 2021-06-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('player', models.IntegerField(primary_key=True, serialize=False)),
                ('map', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('points', models.IntegerField()),
                ('current', models.IntegerField()),
            ],
        ),
    ]