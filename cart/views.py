from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Product

# Create your views here - CART.
def view_cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request):

    # Get the product we're adding
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)

    # Get the current cart
    cart = request.session.get('cart', {})
    
    # Update the cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere - testing to make sure items are added with HttpResponse
    return HttpResponse(cart[id])