from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_verification, name='submit_verification'),
    path('detail/', views.verification_detail, name='verification_detail'),
    path('verify/<int:user_id>/', views.verify_profile, name='verify_profile'),
    
]

