from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product, ItemRequirements
from .forms import ItemRequirementsForm

# Create your views here - PRODUCTS.

def get_products(request): 
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def product_detail(request, pk):
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=pk)
    item_requirements = ItemRequirements.objects.all()
    if request.method == "POST":
        form = ItemRequirementsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.save()
            # return redirect('view_cart')
    else:
        form = ItemRequirementsForm()
    return render(request, 'products/productdetail.html', {'product': product, 'products': products, 'form': form})