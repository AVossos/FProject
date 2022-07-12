from platform import platform
#from turtle import title
from django.db import models

# Create your models here.
class Game(models.Model):
    CONSOLE_CHOICES = [('P', 'PS5'), ('X', 'XBOX'), ('C', 'PC')]
    title=models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, null=True)
    platform = models.CharField(max_length=1, choices=CONSOLE_CHOICES, blank=False)
    gametype = models.CharField(max_length=50, blank=True)
    #image = models.ImageField(upload_to='img', height_field=1024, width_field=1024, max_length=100)



    def __str__(self):
        return self.title
    
    

