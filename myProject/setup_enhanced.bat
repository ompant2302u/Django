@echo off
echo 🚀 Setting up ShopEasy E-Commerce Platform...
echo.

REM Check if virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo ⚠️  Virtual environment not activated!
    echo Please activate it first:
    echo   ..\myvenv\Scripts\activate
    exit /b 1
)

echo ✅ Virtual environment detected
echo.

REM Install requirements
echo 📦 Installing dependencies...
pip install -q -r requirements.txt
echo ✅ Dependencies installed
echo.

REM Run migrations
echo 🗄️  Running database migrations...
python manage.py makemigrations
python manage.py migrate
echo ✅ Database setup complete
echo.

REM Collect static files
echo 📁 Collecting static files...
python manage.py collectstatic --noinput
echo ✅ Static files collected
echo.

echo 👤 Creating admin user...
echo.
python manage.py createsuperuser

echo.
echo 🎉 Setup complete!
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   Main site: http://127.0.0.1:8000/
echo   Admin panel: http://127.0.0.1:8000/admin/
echo.
echo 📝 Don't forget to add products in the admin panel!
pause
