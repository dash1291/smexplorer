from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    response = render(request, 'index.html', {})
    return response

