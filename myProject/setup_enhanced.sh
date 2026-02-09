#!/bin/bash

echo "🚀 Setting up ShopEasy E-Commerce Platform..."
echo ""

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Virtual environment not activated!"
    echo "Please activate it first:"
    echo "  Windows: ..\\myvenv\\Scripts\\activate"
    echo "  Linux/Mac: source ../myvenv/bin/activate"
    exit 1
fi

echo "✅ Virtual environment detected"
echo ""

# Install requirements
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate
echo "✅ Database setup complete"
echo ""

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput
echo "✅ Static files collected"
echo ""

# Check if superuser exists
echo "👤 Checking for admin user..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); exit(0 if User.objects.filter(is_superuser=True).exists() else 1)"

if [ $? -ne 0 ]; then
    echo "⚠️  No admin user found. Creating one..."
    echo ""
    python manage.py createsuperuser
else
    echo "✅ Admin user already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  Main site: http://127.0.0.1:8000/"
echo "  Admin panel: http://127.0.0.1:8000/admin/"
echo ""
echo "📝 Don't forget to add products in the admin panel!"
