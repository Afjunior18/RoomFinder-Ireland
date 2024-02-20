from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# def test(request):
#    return HttpResponse("Testing")

def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def add_room(request):
    return render(request, 'add_room.html')

def search_room(request):
    return render(request, 'search_room.html')

def room_finder(request):
    return render(request, 'room_finder.html')