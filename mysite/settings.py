"""

Django settings for mysite project.


Generated by 'django-admin startproject' using Django 3.2.25.


For more information on this file, see

https://docs.djangoproject.com/en/3.2/topics/settings/


For the full list of settings and their values, see

https://docs.djangoproject.com/en/3.2/ref/settings/

"""


from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!

mystr = 'django-insecure-z7u%0#!1aey0ly6ezr6dh)ng#!x_*(=lhuname_%n-36q7t!h7'

SECRET_KEY = mystr

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    "debug_toolbar",

    'website.apps.WebsiteConfig',
    
    'blog'

]

SITE_ID = 2 # sites framework

ROBOTS_USE_HOST = False    # robots.txt DisAllow HostName
ROBOTS_USE_SITEMAP = False  # robots.txt DisAllow Sitemap


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    "debug_toolbar.middleware.DebugToolbarMiddleware",


]

 
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR/'templates'],

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


WSGI_APPLICATION = 'mysite.wsgi.application'

# Database

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }
}

# Password validation

# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators


def jls_extract_def():

    a = 'django.contrib.auth.password_validation'
    b = '.UserAttributeSimilarityValidator'
    return a+b


def jls_extract_def2():
    a = 'django.contrib.auth.password_validation'
    b = '.UserAttributeSimilarityValidator'
    return a+b


AUTH_PASSWORD_VALIDATORS = [

 {'NAME': jls_extract_def(),

  },

 {

  'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',

 },

 {

  'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',

 },

 {

  'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',

 }

]

# Internationalization

# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'


USE_I18N = True


USE_L10N = True


USE_TZ = True

# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / 'statics', 'medias'
    ]

# Default primary key field typee

# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]
