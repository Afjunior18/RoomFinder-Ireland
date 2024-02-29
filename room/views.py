from django.shortcuts import render
from django.http import HttpResponse

from .models import Room


# Create your views here.

def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def add_room(request):
    return render(request, 'add_room.html')

def room_finder(request):
    rooms = Room.objects.all()
    return render(request, 'room_finder.html', {'rooms': rooms})

def contact(request):
    return render(request, 'contact.html')
