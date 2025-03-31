from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import ChatRoomViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'rooms', ChatRoomViewSet, basename='chatroom')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('api/', include(router.urls)),
    path('room/<room_id>/', views.chat_room, name='chat_room'),

]
