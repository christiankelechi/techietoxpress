"""
Django settings for techietoxpress project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
# github token
# 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
# order
# 5338177865
# root password
# zvU5li63X03QBK0iCp
# 
# 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

# api token
# UCZ63GJ6BUJFGL665OF6UQAQRXP9MMH6

# https://oauth2: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@github.com/christiankelechi/techietoxpress.git
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)llyy_56vbb(#(xi@z8(qkcamhiva4e%65gbq2f&d@8tn53)5x'

# SECURITY WARNING: don't run with debug turned on in production!
# dev mode
# DEBUG = True
# prod mode
DEBUG=False
ALLOWED_HOSTS = ['techietoxpress.com','www.techietoxpress.com','142.11.195.156','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baseapp',
    'blog',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  
]


ROOT_URLCONF = 'techietoxpress.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'baseapp/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'techietoxpress.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# deployment stage
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.psycopg2',
        'NAME': 'techietoxpressdb',
        'USER':'techietoxpressdbuser',
        'PASSWORD':'Kelechi1999!',
        'PORT':'',
        'HOST':'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# dev stage
# STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
# production stage
STATIC_ROOT=os.path.join(BASE_DIR,'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
