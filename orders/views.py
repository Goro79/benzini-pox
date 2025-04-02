from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()

            # Optionally notify workers
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "workers_group",
                {
                    "type": "order_notification",
                    "order_id": order.id,
                    "message": "New auto order received!"
                }
            )

            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

#@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})
