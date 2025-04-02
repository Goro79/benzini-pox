from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Welcome to the Say Lawn Project!")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Use custom accounts URLs
    path('chat/', include('chat.urls')),          # Include chat app URLs
    path('orders/', include('orders.urls')),
    path('verification/', include('verification.urls')),      # Include orders app URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)