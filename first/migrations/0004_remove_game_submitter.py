# Generated by Django 4.0.3 on 2022-04-09 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_remove_game_vaccinations_game_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='submitter',
        ),
    ]