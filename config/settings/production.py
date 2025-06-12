from .base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    ),
    'ENGINE': 'django.db.backends.postgresql',
}

ALLOWED_HOSTS = ['https://ashisane.onrender.com', 'render.com']

# Security best practices for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

