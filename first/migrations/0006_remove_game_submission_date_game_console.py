# Generated by Django 4.0.3 on 2022-04-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_game_age_remove_game_breed_remove_game_sex_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='submission_date',
        ),
        migrations.AddField(
            model_name='game',
            name='console',
            field=models.CharField(blank=True, choices=[('P', 'PS5'), ('X', 'XBOX'), ('C', 'PC')], max_length=1),
        ),
    ]
