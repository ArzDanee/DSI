from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-game'),
    path('<slug>', views.game, name='game'),

]