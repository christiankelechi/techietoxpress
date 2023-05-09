from .base import *
DEBUG = False
ADMINS = [
 ('kc','kezechristian@gmail.com'),
]
ALLOWED_HOSTS = ['techietoxpress.com','www.techietoxpress.com','74.208.95.231','localhost']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'techietoxpressdatabase',
#         'USER':'techietoxpressdatabaseuser',
#         'PASSWORD':'Kelechi1999!',
#         'PORT':'',
#         'HOST':'localhost'
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
 }
}
# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True