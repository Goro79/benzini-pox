from django.urls import path, include
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    # Optionally, include other Django auth URLs:
    path('', include('django.contrib.auth.urls')),
]
