from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        payment_form = PaymentForm(request.POST or None)
        # Get shipping Session Data
        my_shipping = request.session.get('shipping_info')
        # Gather Order Info
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        amount_paid = totals

        # Get Shipping Address data form Session "my_shipping"
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        
        if request.user.is_authenticated:
            user = request.user
            # create Oder
            create_order = Order(user=user, full_name=full_name, email=email, Shipping_Address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            messages.success(request,"Order Placed")
            return redirect('home')
        else:
            create_order = Order(user=user, full_name=full_name, email=email, Shipping_Address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            messages.success(request,"Order Placed")
            return redirect('home')
            
    else:
        messages.success(request,"Access Denied")
        return redirect('home')

def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # create a session with Shipping Info

        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        if request.user.is_authenticated:
            #Get the billing form
            billing_form = PaymentForm()
            return render(request, 'billing_info.html', {'cart_products': cart_products, 'quantities': quantities, 'totals': totals, 'shipping_info': request.POST, 'billing_form':billing_form})
        else:
            billing_form = PaymentForm()
            return render(request, 'billing_info.html', {'cart_products': cart_products, 'quantities': quantities, 'totals': totals, 'shipping_info': request.POST, 'billing_form':billing_form})
    else:
        messages.success(request,"Access Denied")
        return redirect('home')

# Create your views here.
def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request,"checkout.html",{'cart_products':cart_products, 'quantities':quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request,"checkout.html",{'cart_products':cart_products, 'quantities':quantities, "totals":totals, "shipping_form":shipping_form})

def payment_success(request):
    return render(request,"payment_success.html", {})

