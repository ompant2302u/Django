# ShopEasy - Modern E-Commerce Platform

A fully functional, modern e-commerce website built with Django featuring a clean UI, shopping cart, wishlist, order management, and more.

## ✨ Features

### User Features
- **User Authentication**: Register, login, and logout functionality
- **Product Browsing**: View products by category with search functionality
- **Shopping Cart**: Add/remove items, update quantities
- **Wishlist**: Save favorite products for later
- **Order Management**: Place orders and view order history
- **User Profile**: View orders, manage wishlist, and account settings
- **Responsive Design**: Works seamlessly on desktop and mobile

### Product Features
- Product categories and filtering
- Featured products section
- Stock management
- Product images
- Related products suggestions
- Out of stock indicators

### Admin Features
- Full Django admin panel access
- Manage products, categories, orders
- User management
- Stock tracking

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Navigate to project directory**
```bash
cd myProject
```

2. **Activate virtual environment**

Windows:
```bash
..\myvenv\Scripts\activate
```

Linux/Mac:
```bash
source ../myvenv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
```

6. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

7. **Run the development server**
```bash
python manage.py runserver
```

8. **Access the website**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
myProject/
├── myApp/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── product.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── profile.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── search.html
│   │   └── category.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── myProject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── manage.py
└── requirements.txt
```

## 🎨 Features Breakdown

### 1. Home Page
- Hero section with call-to-action
- Category navigation
- Featured products showcase
- All products grid
- Newsletter subscription

### 2. Product Detail Page
- Large product image
- Product information and description
- Stock availability indicator
- Add to cart button
- Add to wishlist button
- Related products section

### 3. Shopping Cart
- View all cart items
- Update quantities with +/- buttons
- Remove items
- See total price
- Proceed to checkout

### 4. Checkout
- Review order items
- Confirm purchase
- Stock validation
- Order creation

### 5. User Profile
- **Orders Tab**: View order history with status
- **Wishlist Tab**: Manage saved products
- **Settings Tab**: View account information

### 6. Search & Filter
- Search products by name or description
- Filter by category
- Real-time category filtering

## 🛠️ Admin Panel Setup

1. Login to admin panel: http://127.0.0.1:8000/admin/
2. Add Categories (e.g., Electronics, Clothing, Books)
3. Add Products with:
   - Name
   - Description
   - Price
   - Category
   - Stock quantity
   - Image (optional)
   - Featured checkbox

## 🎯 Key Improvements

### Backend
- ✅ Enhanced error handling and validation
- ✅ Stock management with quantity checks
- ✅ Order tracking system
- ✅ Wishlist functionality
- ✅ Optimized database queries with select_related
- ✅ Transaction safety for checkout
- ✅ User feedback with Django messages

### Frontend
- ✅ Modern, clean UI with Inter font
- ✅ Smooth animations and transitions
- ✅ Responsive design for all devices
- ✅ Interactive quantity controls
- ✅ Real-time cart count
- ✅ Toast notifications for user actions
- ✅ Empty state designs
- ✅ Loading states and hover effects

### User Experience
- ✅ Intuitive navigation
- ✅ Clear call-to-actions
- ✅ Stock availability indicators
- ✅ Related products suggestions
- ✅ Wishlist for saving favorites
- ✅ Order history tracking
- ✅ Search functionality

## 🔧 Configuration

### Settings to Review
- `MEDIA_ROOT` and `MEDIA_URL` for product images
- `STATIC_ROOT` and `STATIC_URL` for static files
- Database configuration in `settings.py`
- Email backend for notifications (optional)

## 📝 Models

### Product
- name, description, price
- category (ForeignKey)
- image, stock, featured
- created_at timestamp

### Category
- name, description
- Related products

### Cart
- user, product, quantity
- added_at timestamp

### Order
- user, total_amount, status
- created_at timestamp

### OrderItem
- order, product, quantity, price

### Wishlist
- user, product
- added_at timestamp

## 🚨 Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic
```

### Database errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Images not displaying
- Check MEDIA_ROOT and MEDIA_URL in settings.py
- Ensure media folder exists
- Verify image uploads in admin panel

## 🎨 Customization

### Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary: #6366f1;
    --secondary: #10b981;
    --danger: #ef4444;
    /* ... */
}
```

### Logo
Change "ShopEasy" text in `templates/base.html`

### Footer
Edit footer content in `templates/base.html`

## 📱 Responsive Breakpoints
- Desktop: > 768px
- Mobile: ≤ 768px

## 🔐 Security Notes
- Change SECRET_KEY in production
- Set DEBUG = False in production
- Configure ALLOWED_HOSTS
- Use environment variables for sensitive data
- Enable HTTPS in production

## 📄 License
This project is open source and available for educational purposes.

## 🤝 Contributing
Feel free to fork, modify, and use this project for learning!

## 📧 Support
For issues or questions, please check the code comments or Django documentation.

---

**Made with ❤️ using Django**
