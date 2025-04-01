from django.db import models
from django.conf import settings

ORDER_TYPE_CHOICES = (
    ('manual', 'Manual Order'),
    ('auto', 'Auto Order'),
)

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
)

class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer_orders'
    )
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='worker_orders'
    )
    order_type = models.CharField(
        max_length=10,
        choices=ORDER_TYPE_CHOICES,
        default='manual'
    )
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    details = models.TextField(blank=True, null=True)  # Additional info

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username} ({self.get_order_type_display()})"


