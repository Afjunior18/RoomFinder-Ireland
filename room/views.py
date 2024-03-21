from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Room
from .forms import RoomForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        context = {
            'add_room_url': reverse('add_room'),
            'room_finder_url': reverse('room_finder'),
            'contact_url': reverse('contact'),
        }
    else:
        context = {
            'register_url': '/accounts/signup/',
            'login_url': '/accounts/login/',
        }

    return render(request, 'index.html', context)


@login_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.room_owner = request.user
            room.owner_email = request.user.email
            if request.user.is_superuser:
                room.is_pending_approval = False
            else:
                room.is_pending_approval = True

            if 'room_image' in request.FILES:
                room.room_image = request.FILES['room_image']

            room.save()

            room_id = room.id

            messages.add_message(
                request, messages.SUCCESS,
                'Room submitted and awaiting approval'
            )
            return redirect('room_finder')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})


def room_finder(request):
    if request.user.is_superuser:
        rooms = Room.objects.all().order_by("-created_on")
    else:
        rooms = (
            Room.objects
            .filter(is_pending_approval=False)
            .order_by("-created_on")
            )
    return render(request, 'room_finder.html', {'rooms': rooms})


def contact(request):
    return render(request, 'contact.html')


@user_passes_test(lambda u: u.is_superuser)
def approve_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.is_pending_approval = False
    room.save()
    messages.success(request, 'Room approved successfully.')
    return redirect('room_finder')


@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.user == room.room_owner or request.user.is_superuser:
        room.delete()
        messages.success(request, 'Room delete succesfully!')

    return redirect('room_finder')


@login_required
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            if not room.is_pending_approval:
                room.is_pending_approval = True
                messages.success(
                    request,
                    'Room edited successfully and is pending approval.'
                    )
            room.save()
            return redirect('room_finder')

    return render(request, 'edit_room.html', {'form': form, 'room': room})
