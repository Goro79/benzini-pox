from django.contrib import admin
from .models import ProfileVerification

@admin.register(ProfileVerification)
class ProfileVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified', 'submitted_at')
    list_filter = ('verified',)
