from django.contrib import admin

from first.models import Game

# Register your models here.
#from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display=['platform', 'title', 'description', 'gametype' ]
