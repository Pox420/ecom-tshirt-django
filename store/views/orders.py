from store.models import Order
from django.views.generic.list import ListView


class OrderListView(ListView):
    template_name = 'store/orders.html'
    model = Order
    paginate_by = 2  # only 2 product will be displayed
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date').exclude(
            order_status="PENDING")
