from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    path('create/', views.create_order, name='create_order'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
]
