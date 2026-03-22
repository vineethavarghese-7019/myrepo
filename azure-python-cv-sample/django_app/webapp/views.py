from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {"title": "Django CV Sample", "message": "Hello from Django!"}
    return render(request, 'index.html', context)
