from .base import *

DEBUG = False

ADMINS = (
    ('Nicola S', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       # 'ENGINE': 'django.db.backends.postgresql',
       # 'NAME': 'educa',
       # 'USER': 'educa',
       # 'PASSWORD': '*****',
   }
}

# SSL config
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
