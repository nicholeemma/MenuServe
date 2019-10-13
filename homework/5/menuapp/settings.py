"""
Django settings for menuapp project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from django.urls import reverse
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ngt-^z+pp9l6nq903m7umy1yto+6fublxy2gjl$n4d2*)80fe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ['WEBSITE_SITE_NAME']+'.azurewebsites.net','127.0.0.1'] if 'WEBSITE_SITE_NAME' in os.environ else []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menuserve',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ROOT_URLCONF = 'menuapp.urls'
# Redirect to home URL after login (Default redirects to /accounts/profile/)
#LOGIN_REDIRECT_URL = '/Manager-Main/'
LOGIN_REDIRECT_URL = "Order"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'menuapp.wsgi.application'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default' :{
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME': os.environ['DBNAME'],
#         'HOST': os.environ['DBHOST'],
#         'USER': os.environ['DBUSER'],
#         'PASSWORD':os.environ['DBPASS'],
#         'OPTIONS':{
#             'sslmode':'require'
#         }
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
# STATICFILES_DIRS = (
#    # ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
#    # ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
#     ('Pictures',os.path.join(STATIC_ROOT,'Pictures').replace('\\','/') ),
#     ('Music',os.path.join(STATIC_ROOT,'Music').replace('\\','/') ),
# )
# media setting
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ROOT_URLCONF = '/'