from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import transaction

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Cart

def home(request):
    # Get ALL products (not just featured)
    products = Product.objects.all()[:8]  # Show first 8 products
    featured_products = Product.objects.filter(featured=True)[:4]
    categories = Category.objects.all()
    
    return render(request, 'home.html', {
        'products': products,  # Pass all products
        'featured_products': featured_products,
        'categories': categories
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product.html', {'product': product})

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'search.html', {
        'products': products,
        'query': query
    })

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'category.html', {
        'category': category,
        'products': products
    })

def profile_view(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    Cart.objects.filter(id=cart_id, user=request.user).delete()
    return redirect('cart')

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('home')

    if request.method == "POST":
        with transaction.atomic():
            for item in cart_items:
                product = item.product

                if product.stock < item.quantity:
                    messages.error(
                        request,
                        f"Not enough stock for {product.name}."
                    )
                    return redirect('checkout')

                # Deduct stock
                product.stock -= item.quantity
                product.save()

            # Clear cart AFTER stock deduction
            cart_items.delete()

        messages.success(request, "Order placed successfully!")
        return redirect('home')

    total = sum(item.total_price() for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })