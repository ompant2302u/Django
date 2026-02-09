from django.core.management.base import BaseCommand
from myApp.models import Category, Product

class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **kwargs):
        # Create categories
        electronics, _ = Category.objects.get_or_create(
            name='Electronics',
            defaults={'description': 'Latest electronic gadgets and devices'}
        )
        
        clothing, _ = Category.objects.get_or_create(
            name='Clothing',
            defaults={'description': 'Trendy fashion and apparel'}
        )
        
        books, _ = Category.objects.get_or_create(
            name='Books',
            defaults={'description': 'Best-selling books and novels'}
        )
        
        home, _ = Category.objects.get_or_create(
            name='Home & Garden',
            defaults={'description': 'Home decor and garden essentials'}
        )

        # Sample products
        products = [
            # Electronics
            {'name': 'Wireless Headphones', 'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life', 'price': 149.99, 'category': electronics, 'stock': 50, 'featured': True},
            {'name': 'Smart Watch', 'description': 'Fitness tracker with heart rate monitor and GPS', 'price': 299.99, 'category': electronics, 'stock': 35, 'featured': True},
            {'name': 'Bluetooth Speaker', 'description': 'Portable waterproof speaker with amazing sound quality', 'price': 79.99, 'category': electronics, 'stock': 60, 'featured': False},
            {'name': 'Laptop Stand', 'description': 'Ergonomic aluminum laptop stand for better posture', 'price': 39.99, 'category': electronics, 'stock': 100, 'featured': False},
            {'name': 'USB-C Hub', 'description': '7-in-1 USB-C hub with HDMI, USB 3.0, and SD card reader', 'price': 49.99, 'category': electronics, 'stock': 75, 'featured': False},
            
            # Clothing
            {'name': 'Cotton T-Shirt', 'description': 'Comfortable 100% cotton t-shirt in various colors', 'price': 24.99, 'category': clothing, 'stock': 200, 'featured': True},
            {'name': 'Denim Jeans', 'description': 'Classic fit denim jeans with stretch comfort', 'price': 59.99, 'category': clothing, 'stock': 150, 'featured': False},
            {'name': 'Hoodie', 'description': 'Cozy fleece hoodie perfect for casual wear', 'price': 44.99, 'category': clothing, 'stock': 120, 'featured': False},
            {'name': 'Running Shoes', 'description': 'Lightweight running shoes with cushioned sole', 'price': 89.99, 'category': clothing, 'stock': 80, 'featured': True},
            {'name': 'Winter Jacket', 'description': 'Warm insulated jacket for cold weather', 'price': 129.99, 'category': clothing, 'stock': 45, 'featured': False},
            
            # Books
            {'name': 'The Great Novel', 'description': 'Bestselling fiction novel of the year', 'price': 19.99, 'category': books, 'stock': 300, 'featured': False},
            {'name': 'Python Programming', 'description': 'Complete guide to Python programming for beginners', 'price': 39.99, 'category': books, 'stock': 150, 'featured': False},
            {'name': 'Cookbook Deluxe', 'description': '500 delicious recipes for every occasion', 'price': 29.99, 'category': books, 'stock': 100, 'featured': False},
            {'name': 'Self-Help Guide', 'description': 'Transform your life with proven strategies', 'price': 24.99, 'category': books, 'stock': 200, 'featured': False},
            
            # Home & Garden
            {'name': 'Plant Pot Set', 'description': 'Set of 3 ceramic plant pots with drainage', 'price': 34.99, 'category': home, 'stock': 90, 'featured': False},
            {'name': 'LED Desk Lamp', 'description': 'Adjustable LED lamp with touch control', 'price': 45.99, 'category': home, 'stock': 70, 'featured': False},
            {'name': 'Throw Pillow', 'description': 'Soft decorative throw pillow for couch', 'price': 19.99, 'category': home, 'stock': 150, 'featured': False},
            {'name': 'Wall Clock', 'description': 'Modern minimalist wall clock', 'price': 29.99, 'category': home, 'stock': 85, 'featured': False},
        ]

        created_count = 0
        for product_data in products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {created_count} new products!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total products in database: {Product.objects.count()}')
        )
