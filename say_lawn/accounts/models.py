from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    is_verified = models.BooleanField(default=False)  # For manual ID verification later
    active_chats = models.ManyToManyField('chat.ChatRoom', blank=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"

class User(AbstractUser):
    # Remove 'username' if you want email-only login
    # or keep it if you want both username + email
    # email = models.EmailField(unique=True)
    # role = models.CharField(
    #     max_length=20,
    #     choices=[('employer', 'Employer'), ('employee', 'Employee')],
    #     default='employee'
    # )
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Must be empty list

    def __str__(self):
        return self.email
    
    