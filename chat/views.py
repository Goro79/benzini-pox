from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def chat_room(request, room_id):
    # Render the chat room template with the room_id passed in the context.
    return render(request, 'chat/chat_room.html', {'room_id': room_id})
