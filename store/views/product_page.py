from math import floor
from store.models import Tshirt
from django.views.generic.detail import DetailView


class ProductDetailView(DetailView):
    template_name = 'store/product_details.html'
    model = Tshirt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        tshirt = context.get('tshirt')
        size = request.GET.get('size')
        if size is None:
            size = tshirt.sizevariant_set.all().order_by('price').first()
        else:
            size = tshirt.sizevariant_set.get(size=size)
        size_price = floor(size.price)
        sell_price = floor(size_price - (size_price * (tshirt.discount / 100)))
        context = {
            'tshirt': tshirt,
            'price': size.price,
            'sell_price': sell_price,
            'active_size': size,
        }
        return context
