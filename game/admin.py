from django.contrib import admin
from .models import Game, Media

# Register your models here.
class MediaInline(admin.TabularInline):
    model = Media

class GameAdmin(admin.ModelAdmin):
    inlines = [MediaInline]

admin.site.register(Game, GameAdmin)
admin.site.register(Media)