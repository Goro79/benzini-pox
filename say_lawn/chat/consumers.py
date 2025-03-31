import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, Message  # if you have these models

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # For dynamic rooms, get 'room_id' from the URL
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        # (Optional) You could verify that the room exists in the database
        # or create it automatically if needed.

        # If authentication is required, you might also check here:
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            # Join the channel group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data.get('message', '')

        # (Optional) Save the message to the database using database_sync_to_async

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_content,
                'sender_id': self.scope["user"].id,
            }
        )

    async def chat_message(self, event):
        message_content = event['message']
        sender_id = event.get('sender_id')
        await self.send(text_data=json.dumps({
            'message': message_content,
            'sender_id': sender_id,
        }))
