from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request, room_id):
    """
    Renders a simple chat UI for the given room.
    For now, no checks on whether the user is allowed in this room.
    """
    context = {
        'room_id': room_id,
    }
    return render(request, 'chat/chat_room.html', context)
