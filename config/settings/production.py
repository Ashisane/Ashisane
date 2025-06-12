from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com', 'render.com']  # update this later

# Security best practices for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True