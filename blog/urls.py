from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name = 'index-blog'),
    path('post/<slug>/', views.post, name = 'post'),
]