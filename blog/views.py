from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')
    paginator = Paginator(latest, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context= {
        'title':'Blog - MotionGames.id',
        'company':'MotionGames.id',
        'ref':'Blog',
        'object_list': featured,
        'latest': latest,
        'page_obj': page_obj
        
    }
    return render(request, 'blog/index.html', context)

def post(request,slug):
    post = Post.objects.get(slug=slug)
    latest = Post.objects.order_by('-timestamp')
    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'blog/post.html', context)
