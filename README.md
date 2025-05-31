# Ywork_assignment

Order Management System with Google OAuth Integration
Overview
This Django-based Order Management System integrates Google OAuth for authentication and JWT tokens for secure API access. The solution uses django-allauth for handling OAuth flows and djangorestframework-simplejwt for token-based API authentication.

System Architecture

Features
Google OAuth 2.0 authentication

JWT token-based API security

CRUD operations for orders

Secure token refresh mechanism

Session-based authentication for web views

API endpoints for mobile clients

User profile management with Google tokens

Technology Stack
Backend: Django 5.0, Django REST Framework

Database: PostgreSQL (SQLite for development)

Authentication: Google OAuth, JWT

Libraries:

django-allauth (OAuth integration)

djangorestframework-simplejwt (JWT authentication)

python-dotenv (environment variables)

Deployment: Docker-ready

Setup Instructions
1. Prerequisites
Python 3.9+

PostgreSQL (for production)

Google OAuth credentials

Git

2. Clone Repository
bash
git clone https://github.com/yourusername/order-management-system.git
cd order-management-system
3. Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
4. Install Dependencies
bash
pip install -r requirements.txt
5. Set Up Environment Variables
Create .env file:

env
# Django Settings
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings (PostgreSQL)
DB_NAME=order_mgmt
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Google OAuth Settings
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
6. Set Up Google OAuth
Go to Google Cloud Console

Create credentials (OAuth Client ID for Web Application)

Add authorized redirect URIs:

http://localhost:8000/accounts/google/login/callback/
http://127.0.0.1:8000/accounts/google/login/callback/
7. Run Migrations
bash
python manage.py migrate
8. Create Superuser (Optional)
bash
python manage.py createsuperuser
9. Run Development Server
bash
python manage.py runserver
API Documentation
Authentication Flow
Initiate Google Login:
GET /accounts/google/login/

Google Redirects Back:
GET /accounts/google/login/callback/ (handled by allauth)

Get JWT Tokens:
GET /api/token/ (requires session cookie)

API Endpoints
Endpoint	Method	Description	Authentication
/api/token/	GET	Get JWT tokens	Session	
/api/orders/	GET	List user's orders	JWT
/api/orders/create/	POST	Create new order	JWT


Example Requests


Create New Order:

http
POST /api/orders/create/ HTTP/1.1
Host: localhost:8000
Authorization: Bearer eyJhbGciOi...
Content-Type: application/json

{
  "title": "Website Redesign",
  "description": "Complete redesign of company website"
}
Successful Response:

json
{
  "id": 5,
  "title": "Website Redesign",
  "description": "Complete redesign of company website",
  "status": "PENDING",
  "created_at": "2023-10-15T12:30:45Z",
  "updated_at": "2023-10-15T12:30:45Z"
}
Security Implementation
1. Secret Management
All secrets stored in .env file

.env added to .gitignore to prevent accidental exposure

Environment variables loaded via python-dotenv

2. Authentication
Google OAuth: For secure third-party authentication

JWT Tokens: Stateless authentication for API endpoints

Session Authentication: For web-based OAuth flow

Token Rotation: Automatic refresh token rotation

Short-lived Tokens: Access tokens expire in 15 minutes

3. Data Protection
Input validation through serializers

Read-only fields for sensitive data

HTTPS enforcement in production

CSRF protection for web views

4. Production Security
python
# settings.py
if not DEBUG:
    # Security headers
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True