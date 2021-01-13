from store.models import Cart
from store.models import Payment
from django.shortcuts import render,redirect

from Tshop.settings import API_KEY, AUTH_TOKEN
from instamojo_wrapper import Instamojo

API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');


def validate_payment(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    payment_request_id = request.GET.get(('payment_request_id'))
    payment_id = request.GET.get(('payment_id'))

    response = API.payment_request_payment_status(payment_request_id, payment_id)

    status = response.get('payment_request').get('payment').get('status')  # Payment status

    if status != "Failed":
        print('payment success')
        try:
            payment = Payment.objects.get(payment_request_id=payment_request_id)
            payment.payment_id = payment_id
            payment.payment_status = status
            payment.save()

            order = payment.order
            order.order_status = "PLACED"
            order.save()

            cart = []
            request.session['cart'] = cart

            Cart.objects.filter(user=user).delete()

            return redirect('orders')
        except:
            return render(request, 'store/payment_failed.html')
    else:
        return render(request, 'store/payment_failed.html')