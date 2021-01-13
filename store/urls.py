from django.urls import path
from store.views import home, cart, signup, LoginView, validate_payment, ProductDetailView, OrderListView
from store.views import signout, checkout, add_to_cart
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart),
    path('signup/', signup),
    path('orders/', login_required(OrderListView.as_view(),login_url='/login'), name='orders'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', signout),
    path('checkout/', checkout, name='checkout'),
    path('product/<str:slug>', ProductDetailView.as_view()),
    path('addtocart/<str:slug>/<str:size>/', add_to_cart),
    path('validate_payment/', validate_payment),
]
