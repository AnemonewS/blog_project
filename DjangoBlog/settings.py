import os.path
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.PortfolioConfig',
    'rest_framework',


    'debug_toolbar',
    'ckeditor',
    'ckeditor_uploader',
    'django_filters',
    'djoser',
    'rest_framework.authtoken',
    'drf_yasg',

    'social_django',
    'oauth2_provider',
    'rest_framework_social_oauth2',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'DjangoBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    '127.0.0.1'
]

CKEDITOR_UPLOAD_PATH = "uploads/"


REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_PAGINATION_CLASS': "rest_framework.pagination.LimitOffsetPagination",
    'PAGE_SIZE': 3

}
# smtp
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "paperworldcomm@gmail.com"
EMAIL_HOST_PASSWORD = "26zerOnine0101brB"
EMAIL_PORT = 587

# djoser_settings
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}

# simpleJWT_settings
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,
#
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,
#
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
#
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#
#     'JTI_CLAIM': 'jti',
#
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }


try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *
