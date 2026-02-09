# ShopEasy - Modern E-commerce Platform

A beautiful, modern e-commerce website built with Django featuring smooth animations, responsive design, and comprehensive shopping features.

## Features

✨ **Modern UI/UX**
- Smooth animations and transitions
- Responsive design for all devices
- Beautiful gradient effects
- Interactive product cards

🛒 **Shopping Features**
- Product catalog with categories
- Shopping cart functionality
- Wishlist system
- Secure checkout process
- Order management
- Stock tracking

👤 **User Features**
- User registration and authentication
- User profile management
- Order history
- Cart persistence

🎨 **Design Highlights**
- Gradient hero sections
- Animated product cards
- Smooth scroll effects
- Toast notifications
- Loading animations
- FAQ accordion

## Setup Instructions

### 1. Activate Virtual Environment

**Windows:**
```bash
cd C:\Users\rajju\OneDrive\Documents\Django
myvenv\Scripts\activate
```

**Linux/Mac:**
```bash
cd /path/to/Django
source myvenv/bin/activate
```

### 2. Install Dependencies

```bash
pip install django pillow
```

### 3. Navigate to Project

```bash
cd myProject
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

### 7. Access Admin Panel

Visit: `http://127.0.0.1:8000/admin/`

Login with your superuser credentials and add:
- Categories
- Products (with images)
- Mark some products as "Featured"

## Project Structure

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
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── myProject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
│   └── products/
├── db.sqlite3
└── manage.py
```

## Models

### Category
- name
- description

### Product
- name
- description
- price
- category (ForeignKey)
- image
- stock
- featured (boolean)
- created_at

### Cart
- user (ForeignKey)
- product (ForeignKey)
- quantity
- added_at

### Wishlist
- user (ForeignKey)
- product (ForeignKey)
- added_at

### Order
- user (ForeignKey)
- total_amount
- status
- created_at

### OrderItem
- order (ForeignKey)
- product (ForeignKey)
- quantity
- price

## Key Features Explained

### Animations
- Fade-in effects on page load
- Hover animations on cards
- Pulse effect on CTA buttons
- Smooth scroll behavior
- Scroll reveal animations

### Shopping Cart
- Add/remove products
- Quantity management
- Real-time total calculation
- Persistent cart (per user)

### Checkout
- Beautiful form design
- Order summary sidebar
- Form validation
- Secure checkout badge

### Admin Panel
- Manage categories
- Add/edit products
- Upload product images
- Track orders
- Manage users

## Customization

### Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary: #4f46e5;
    --secondary: #06b6d4;
    --dark: #111827;
    --gray: #6b7280;
    --light: #f9fafb;
}
```

### Logo
Change "ShopEasy" in `templates/base.html`:
```html
<a href="{% url 'home' %}" class="logo">YourBrand</a>
```

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Issues
```bash
python manage.py flush
python manage.py migrate
```

### Port Already in Use
```bash
python manage.py runserver 8080
```

## Future Enhancements

- [ ] Payment gateway integration
- [ ] Product reviews and ratings
- [ ] Advanced search filters
- [ ] Email notifications
- [ ] Social media login
- [ ] Product recommendations
- [ ] Discount codes/coupons
- [ ] Multi-language support

## Technologies Used

- **Backend:** Django 6.0
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Icons:** Font Awesome 6.4
- **Fonts:** Google Fonts (Inter)

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please create an issue in the repository.

---

Made with ❤️ for Django Students
