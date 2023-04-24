from django.shortcuts import render
from django.db.models import Q
from blog.models import Post
from game.models import Game

def index(request):
    context = {
        'title':'Home - MotionGames.id',
        'company':'MotionGames.id',

    }
    return render(request, 'index.html', context)

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if query is not None:
            post_lookups = Q(title__icontains=query) | Q(content__icontains=query) | Q(category__icontains=query)
            game_lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query)
            post_results = Post.objects.filter(post_lookups).distinct()
            game_results = Game.objects.filter(game_lookups).distinct()

            context = { 'post_results': post_results,
                        'query': query,
                        'game_results': game_results,
                        'total_result' : game_results.count() + post_results.count(),
                        'submitbutton': submitbutton,
                        'title': query +' | Search - MotionGames.id',
                        'company':'MotionGames.id',}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html', {'title': 'Not Found | Search - MotionGames.id',
                        'company':'MotionGames.id',})

    else:
        return render(request, 'search.html', {'title': 'Not Found | Search - MotionGames.id',
                        'company':'MotionGames.id',})

