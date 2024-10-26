from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request,"cart_summary.html",{'cart_products':cart_products, 'quantities':quantities, "totals":totals})


def cart_add(request):
    # Get the cart
    cart  = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_Qty = int(request.POST.get('product_Qty'))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #Save to session
        cart.add(product=product, quantity=product_Qty)

        #Get cart Quantity
        cart_quantity = cart.__len__()

        # Return response 
        # response = JsonResponse({'Product Name:':product.name})
        response = JsonResponse({'Qty':cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request, ("Item Successfully Deleted From Cart..."))

        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_Qty'))

        #print(f'Product ID: {product_id}, Quantity: {product_qty}')
        
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
        messages.success(request, ("Your Cart Has Been Updated..."))
        return response
        

