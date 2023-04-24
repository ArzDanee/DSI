from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Career - MotionGames.id',
        'company':'MotionGames.id',
        'ref':'Career',

    }
    return render(request, 'career/index.html', context)
