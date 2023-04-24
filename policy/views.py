from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def privacy_policy(request):
    with open(file='/static_cdn/doc/lorem-ipsum.pdf',mode='rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=lorem-ipsum.pdf'
        return response
    
def term_of_services(request):
    with open('/static_cdn/doc/lorem-ipsum2.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response

def legal_information(request):
    with open('/static_cdn/doc/lorem-ipsum3.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response
