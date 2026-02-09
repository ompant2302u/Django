# Commands to Run

## Step-by-Step Setup

### 1. Navigate to Project Directory
```bash
cd C:\Users\rajju\OneDrive\Documents\Django\myProject
```

### 2. Activate Virtual Environment
```bash
# Windows
..\myvenv\Scripts\activate

# Linux/Mac
source ../myvenv/bin/activate
```

### 3. Create Migrations
```bash
python manage.py makemigrations
```

Expected output:
```
Migrations for 'myApp':
  myApp/migrations/0002_wishlist_order_orderitem.py
    - Create model Wishlist
    - Create model Order
    - Create model OrderItem
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

Expected output:
```
Running migrations:
  Applying myApp.0002_wishlist_order_orderitem... OK
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

You'll be prompted:
```
Username: admin
Email: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 7. Open in Browser
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Quick Commands Reference

### Database Management
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (WARNING: Deletes all data)
python manage.py flush

# Create database backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```

### User Management
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword <username>
```

### Server Management
```bash
# Run server (default port 8000)
python manage.py runserver

# Run on different port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Clear static files
python manage.py collectstatic --clear
```

### Development
```bash
# Check for issues
python manage.py check

# Open Django shell
python manage.py shell

# Show migrations
python manage.py showmigrations

# SQL for migration
python manage.py sqlmigrate myApp 0001
```

## Troubleshooting Commands

### If migrations fail:
```bash
# Delete migration files (except __init__.py)
# Then run:
python manage.py makemigrations
python manage.py migrate
```

### If port is in use:
```bash
# Find process using port 8000 (Windows)
netstat -ano | findstr :8000

# Kill process (Windows)
taskkill /PID <process_id> /F

# Or use different port
python manage.py runserver 8080
```

### If static files not loading:
```bash
python manage.py collectstatic --noinput
```

### If database is corrupted:
```bash
# Backup first!
python manage.py dumpdata > backup.json

# Delete db.sqlite3
# Then:
python manage.py migrate
python manage.py loaddata backup.json
```

## Testing Commands

### Test specific app:
```bash
python manage.py test myApp
```

### Run with verbosity:
```bash
python manage.py test --verbosity=2
```

### Check deployment readiness:
```bash
python manage.py check --deploy
```

## Production Commands (Future)

### Collect static files:
```bash
python manage.py collectstatic --noinput
```

### Create requirements file:
```bash
pip freeze > requirements.txt
```

### Install from requirements:
```bash
pip install -r requirements.txt
```

## Git Commands (Optional)

### Initialize repository:
```bash
git init
git add .
git commit -m "Initial commit with all enhancements"
```

### Create .gitignore:
```
*.pyc
__pycache__/
db.sqlite3
media/
.env
venv/
myvenv/
*.log
```

## Daily Development Workflow

1. Activate virtual environment
2. Run server: `python manage.py runserver`
3. Make changes to code
4. If models changed:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
5. Test in browser
6. Commit changes (if using git)

## Common Tasks

### Add new product via admin:
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser
3. Click "Products" → "Add Product"
4. Fill form and save

### View database in admin:
- Categories: /admin/myApp/category/
- Products: /admin/myApp/product/
- Cart: /admin/myApp/cart/
- Wishlist: /admin/myApp/wishlist/
- Orders: /admin/myApp/order/

### Clear all carts:
```bash
python manage.py shell
>>> from myApp.models import Cart
>>> Cart.objects.all().delete()
>>> exit()
```

### Make all products featured:
```bash
python manage.py shell
>>> from myApp.models import Product
>>> Product.objects.all().update(featured=True)
>>> exit()
```

## Performance Optimization

### Create database indexes:
```bash
python manage.py migrate
```

### Optimize images (manual):
- Use WebP format
- Compress before upload
- Max size: 1MB

## Backup Strategy

### Daily backup:
```bash
python manage.py dumpdata > backups/backup_$(date +%Y%m%d).json
```

### Restore backup:
```bash
python manage.py loaddata backups/backup_20260209.json
```

## Environment Variables (Future)

Create `.env` file:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

## Useful Django Shell Commands

```python
# Open shell
python manage.py shell

# Import models
from myApp.models import Product, Category, Cart

# Get all products
Product.objects.all()

# Get featured products
Product.objects.filter(featured=True)

# Create category
Category.objects.create(name="Electronics", description="Electronic items")

# Count products
Product.objects.count()

# Get product by ID
Product.objects.get(id=1)

# Update product
product = Product.objects.get(id=1)
product.price = 99.99
product.save()

# Delete product
Product.objects.get(id=1).delete()
```

## Quick Reference

| Task | Command |
|------|---------|
| Start server | `python manage.py runserver` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Create admin | `python manage.py createsuperuser` |
| Open shell | `python manage.py shell` |
| Check errors | `python manage.py check` |
| Collect static | `python manage.py collectstatic` |

---

**Remember:** Always activate virtual environment before running commands!

**Windows:** `..\myvenv\Scripts\activate`
**Linux/Mac:** `source ../myvenv/bin/activate`
