from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        #Get billing info from the last page
        payment_form = PaymentForm(request.POST or None)
        # Get shipping Session Data
        my_shipping = request.session.get('my_shipping')
        # Gather Order Info
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        amount_paid = totals

        # Get Shipping Address data form Session "my_shipping"
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        
        # If user is not authenticated
        user = None

        if request.user.is_authenticated:
            user = request.user
            # create Oder
            create_order = Order(user=user, full_name=full_name, email=email, Shipping_Address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            # Add Order Items
            # Get the Order ID
            order_id = create_order.pk
            # Get product Stuff
            for product in cart_products():
                # Get product ID
                product_id = product.id
                # Get Product Price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                # Get Quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # Create Order Item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
                        create_order_item.save()
            for key in list(request.session.keys()):
                if key == "session_key":    
                    del request.session[key]
                            

            messages.success(request,"Order Placed")
            return redirect('home')
        else:
            create_order = Order(user=user, full_name=full_name, email=email, Shipping_Address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            order_id = create_order.pk
            # Get product Stuff
            for product in cart_products():
                # Get product ID
                product_id = product.id
                # Get Product Price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                # Get Quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # Create Order Item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                        create_order_item.save()
            # Delete the cart
            for key in list(request.session.keys()):
                if key == "session_key":    
                    del request.session[key]
                            
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

