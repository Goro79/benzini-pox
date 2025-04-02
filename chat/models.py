from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_rooms')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room between {self.customer} and {self.worker}"

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in room {self.room.id}"
