# Generated by Django 4.0.3 on 2022-04-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='breed',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='game',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AddField(
            model_name='game',
            name='species',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='submission_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='submitter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='vaccinations',
            field=models.ManyToManyField(blank=True, to='first.vaccine'),
        ),
    ]
