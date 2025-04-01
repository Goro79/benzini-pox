import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get room id from URL kwargs and create a group name
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        # Set default display name (for anonymous users, you may update this later)
        self.nickname = "Anonymous"

        # If user is authenticated, you might check a property to differentiate role:
        if self.scope.get("user") and self.scope["user"].is_authenticated:
            # Check if the user is an employee (assuming your User model has 'is_employee')
            if getattr(self.scope["user"], "is_employee", False):
                self.nickname = f"Employee: {self.scope['user'].username}"
            else:
                self.nickname = f"Customer: {self.scope['user'].username}"

        # Join the group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"Connected {self.channel_name} as {self.nickname} in group {self.room_group_name}")

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print(f"Disconnected {self.channel_name} from group {self.room_group_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")
        # Optionally, update nickname if the client sends one
        if data.get("nickname"):
            self.nickname = data["nickname"]

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",  # This calls the chat_message handler below
                "message": message,
                "sender": self.nickname,  # Use the friendly nickname
            }
        )
        print(f"Broadcasting message from {self.nickname}: {message}")

    async def chat_message(self, event):
        # Handler called when a message is broadcast to the group
        message = event["message"]
        sender = event["sender"]
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender,
        }))
