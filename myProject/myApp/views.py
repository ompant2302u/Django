from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import transaction
from django.db.models import Q, Count
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, Category, Cart, Order, OrderItem, Wishlist

def home(request):
    products = Product.objects.filter(stock__gt=0).order_by('-created_at')[:12]
    featured_products = Product.objects.filter(featured=True, stock__gt=0)[:4]
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    
    return render(request, 'home.html', {
        'products': products,
        'featured_products': featured_products,
        'categories': categories
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    in_wishlist = False
    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()
    
    return render(request, 'product.html', {
        'product': product,
        'related_products': related_products,
        'in_wishlist': in_wishlist
    })

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    ) if query else Product.objects.none()
    
    return render(request, 'search.html', {
        'products': products,
        'query': query
    })

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(stock__gt=0)
    categories = Category.objects.all()

    return render(request, 'category.html', {
        'category': category,
        'products': products,
        'categories': categories
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    return render(request, 'contact.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Your account has been created.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product').order_by('-created_at')
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    
    # Add item totals to each order item
    for order in orders:
        for item in order.items.all():
            item.item_total = item.quantity * item.price
    
    return render(request, 'profile.html', {
        'user': request.user,
        'orders': orders,
        'wishlist_items': wishlist_items
    })

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if product.stock <= 0:
        messages.error(request, f'{product.name} is out of stock.')
        return redirect('product_detail', product_id=product_id)
    
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'{product.name} quantity updated in cart.')
        else:
            messages.warning(request, f'Cannot add more. Only {product.stock} items available.')
    else:
        messages.success(request, f'{product.name} added to cart.')
    
    return redirect('cart')

@login_required
def update_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'increase':
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
                cart_item.save()
                messages.success(request, f'Updated {cart_item.product.name} quantity.')
            else:
                messages.warning(request, f'Cannot add more. Only {cart_item.product.stock} items available.')
        
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, f'Updated {cart_item.product.name} quantity.')
            else:
                cart_item.delete()
                messages.info(request, f'{cart_item.product.name} removed from cart.')
    
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.info(request, f'{product_name} removed from cart.')
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')

    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('home')

    if request.method == "POST":
        with transaction.atomic():
            total_amount = sum(item.total_price() for item in cart_items)
            
            # Create order
            order = Order.objects.create(
                user=request.user,
                total_amount=total_amount,
                status='pending'
            )
            
            # Process each cart item
            for item in cart_items:
                if item.product.stock < item.quantity:
                    order.delete()
                    messages.error(request, f"Not enough stock for {item.product.name}. Only {item.product.stock} available.")
                    return redirect('checkout')
                
                # Create order item
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                
                # Deduct stock
                item.product.stock -= item.quantity
                item.product.save()
            
            # Clear cart
            cart_items.delete()
            
            messages.success(request, f"Order #{order.id} placed successfully!")
            return redirect('profile')

    total = sum(item.total_price() for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        messages.success(request, f'{product.name} added to wishlist.')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')
    
    return redirect('product_detail', product_id=product_id)

@login_required
def remove_from_wishlist(request, product_id):
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product_id=product_id)
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    messages.info(request, f'{product_name} removed from wishlist.')
    return redirect('profile')
