# 🍽️ Restaurant Management API

A Django REST Framework backend for managing restaurant operations, including user authentication, menu items, orders, and table bookings.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## 🔧 Features

- **Role-based access control** (Admin, Manager, Customer)
- **JWT Authentication** with refresh tokens
- **Menu Management** (CRUD operations)
- **Order Processing** with status tracking
- **Table Booking System**
- **Swagger/OpenAPI Documentation**

## 📦 Installation

### Prerequisites
- Python 3.8+
- PostgreSQL (or SQLite for development)
- Git

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/restaurant-api.git
cd restaurant-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
nano .env  # Edit with your settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
