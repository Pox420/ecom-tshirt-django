from store.forms.authforms import CustomerCreationForm, CusomerAuthForm
from django.contrib.auth import authenticate, login as loginUser, logout
from store.models import SizeVariant, Cart
from django.shortcuts import render, redirect
from django.views.generic.base import View

class LoginView(View):
    def get(self,request):
        form = CusomerAuthForm()
        next_page = request.GET.get('next')
        if next_page is not None:
            request.session['next_page'] = next_page
        return render(request, 'store/login.html', context={"form": form})

    def post(self,request):
        form = CusomerAuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                loginUser(request, user)

                session_cart = request.session.get('cart')
                if session_cart is None:
                    session_cart = []
                else:
                    for c in session_cart:
                        size = c.get('size')
                        tshirt_id = c.get('tshirt')
                        quantity = c.get('quantity')
                        cart_obj = Cart()
                        cart_obj.sizeVariant = SizeVariant.objects.get(size=size, tshirt=tshirt_id)
                        cart_obj.quantity = quantity
                        cart_obj.user = user
                        cart_obj.save()

                cart = Cart.objects.filter(user=user)
                session_cart = []
                for c in cart:
                    obj = {
                        'size': c.sizeVariant.size,
                        'tshirt': c.sizeVariant.tshirt.id,
                        'quantity': c.quantity,
                    }
                    session_cart.append(obj)
                request.session['cart'] = session_cart
                next_page = request.session.get('next_page')
                if next_page is None:
                    next_page = 'home'
                return redirect(next_page)
        else:
            return render(request, 'store/login.html', context={"form": form})

def signup(request):
    if request.method == 'GET':
        form = CustomerCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'store/signup.html', context=context)
    else:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'store/signup.html', context=context)


def signout(request):
    logout(request)
    return redirect('home')