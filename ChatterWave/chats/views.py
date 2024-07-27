# chats/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    
    if not username:
        return render(request, 'error.html', {"error": "Username is required"}, status=400)

    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        logger.error(f"Room with name '{room}' does not exist.")
        return render(request, '404.html', {"error": "Room not found"}, status=404)

    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

# chats/views.py
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)

def checkview(request):
    if request.method == 'POST':
        room = request.POST.get('room_name')
        username = request.POST.get('username')

        # Debugging: Log the received data
        logger.debug(f"Received POST data: room_name={room}, username={username}")

        if Room.objects.filter(name=room).exists():
            return redirect(f'/{room}/?username={username}')
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect(f'/{room}/?username={username}')
    else:
        return HttpResponse("Bad Request", status=400)

def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')

    if not message or not username or not room_id:
        return HttpResponse("Message, username, and room ID are required", status=400)

    try:
        room = Room.objects.get(id=room_id)
        new_message = Message.objects.create(value=message, user=username, room=room)
        new_message.save()
        return HttpResponse("Message sent successfully!")
    except Room.DoesNotExist:
        return HttpResponse("Room does not exist", status=404)

def getMessages(request, room):
    try:
        room_details = Room.objects.get(name=room)
        messages = Message.objects.filter(room=room_details).values()
        return JsonResponse({"messages": list(messages)})
    except Room.DoesNotExist:
        return JsonResponse({"error": "Room not found"}, status=404)
