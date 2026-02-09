@echo off
echo ========================================
echo ShopEasy - Setup Script
echo ========================================
echo.

echo [1/5] Activating virtual environment...
call ..\myvenv\Scripts\activate
echo ✓ Virtual environment activated
echo.

echo [2/5] Installing dependencies...
pip install django pillow
echo ✓ Dependencies installed
echo.

echo [3/5] Creating migrations...
python manage.py makemigrations
echo ✓ Migrations created
echo.

echo [4/5] Applying migrations...
python manage.py migrate
echo ✓ Migrations applied
echo.

echo [5/5] Setup complete!
echo.
echo ========================================
echo Next Steps:
echo ========================================
echo 1. Create superuser: python manage.py createsuperuser
echo 2. Run server: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000/
echo 4. Admin: http://127.0.0.1:8000/admin/
echo ========================================
echo.

pause
