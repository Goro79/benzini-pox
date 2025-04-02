from django.db import models
from django.conf import settings

class ProfileVerification(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='verification')
    face_photo = models.ImageField(upload_to='verification/face_photos/')
    passport_photo = models.ImageField(upload_to='verification/passport_photos/')
    permit_file = models.FileField(upload_to='verification/permit_files/', blank=True, null=True)
    verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Verification for {self.user.username}"
