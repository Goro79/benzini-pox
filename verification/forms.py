from django import forms
from .models import ProfileVerification

class ProfileVerificationForm(forms.ModelForm):
    class Meta:
        model = ProfileVerification
        fields = ['face_photo', 'passport_photo', 'permit_file']
