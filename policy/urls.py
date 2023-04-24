from django.urls import path
from . import views

urlpatterns = [
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('term_of_services/', views.term_of_services, name='term_of_services'),
    path('legal_information/', views.legal_information, name='legal_information'),
]