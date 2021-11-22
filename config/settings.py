import os
import os.path
from pathlib import Path

ENV = True if os.getenv('DJANGO_ENV') == 'production' else False

BASE_DIR = Path(__file__).resolve().parent.parent

if ENV:
    READ_DATABASE = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_READ_DATABASE_NAME'),
        'USER': os.getenv('DJANGO_READ_DATABASE_USER'),
        'PASSWORD': os.getenv('DJANGO_READ_DATABASE_PASSWORD'),
        'HOST': os.getenv('DJANGO_READ_DATABASE_HOST'),
        'PORT': os.getenv('DJANGO_READ_DATABASE_PORT'),
    }

    WRITE_DATABASE = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_WRITE_DATABASE_NAME'),
        'USER': os.getenv('DJANGO_WRITE_DATABASE_USER'),
        'PASSWORD': os.getenv('DJANGO_WRITE_DATABASE_PASSWORD'),
        'HOST': os.getenv('DJANGO_WRITE_DATABASE_HOST'),
        'PORT': os.getenv('DJANGO_WRITE_DATABASE_PORT'),
    }
else:
    READ_DATABASE = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    WRITE_DATABASE = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

# SECRET_KEY = \
#     os.getenv('DJANGO_SECRET_KEY') if ENV else 'django-insecure-2b7bv)@8r9ebu8^x*ud4#rfkq4jh!q67vx@#c@a1dg@m83#wu%'
SECRET_KEY = 'django-insecure-2b7bv)@8r9ebu8^x*ud4#rfkq4jh!q67vx@#c@a1dg@m83#wu%'
ALGORITHM = 'HS256'

DEBUG = False if ENV else True

ALLOWED_HOSTS = [
    # 'localhost',
    # '127.0.0.1',
    # 'web' if ENV else ''
    '*'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'check',
    'docs',
    'index',
    'info',
    'score',
    'recruit',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASE_ROUTERS = ['config.router.DatabaseRouter']

DATABASES = {
    'default': READ_DATABASE,
    'read': READ_DATABASE,
    'write': WRITE_DATABASE,
}

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


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = os.getenv('static_cdn_link') + 'static/' if ENV else '/static/'

STATICFILES_DIRS = [
    os.path.join('static')
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.User'

AWS_S3_BUCKET = os.getenv('aws_s3_bucket')

STATIC_CDN_LINK = os.getenv('static_cdn_link')
