from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Room


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        context = {
            'add_room_url': reverse('add_room'),
            'room_finder_url': reverse('room_finder'),
            'about_url': reverse('about'),
            'contact_url': reverse('contact'),
        }
    else:
        context = {
            'register_url': '/accounts/signup/',
            'login_url': '/accounts/login/',
        }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def add_room(request):
    return render(request, 'add_room.html')


def room_finder(request):
    rooms = Room.objects.all().order_by("-created_on")
    return render(
        request,
        'room_finder.html', 
        {'rooms': rooms},
        )
    


def contact(request):
    return render(request, 'contact.html')

