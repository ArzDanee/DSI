from django.shortcuts import render
from .models import Game
# Create your views here.

def index(request):
    latest = Game.objects.order_by('-updated')
    featured = Game.objects.filter(featured=True).order_by('-updated')[:4]

    context = {
        'title':'Games - MotionGames.id',
        'company':'MotionGames.id',
        'ref':'Games',
        'latest': latest,
        'featured': featured,

    }
    return render(request, 'game/index.html', context)

def game(request,slug):
    game = Game.objects.get(slug=slug)
    context = {
        'game': game,
    }
    return render(request, 'game/game.html', context)