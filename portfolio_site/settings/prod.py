from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_var('DATABASE_NAME'),
        'USER': get_env_var('DATABASE_USER'),
        'PASSWORD': get_env_var('DATABASE_PASSWORD'),
        'HOST': get_env_var('DATABASE_HOST'),
        'PORT': get_env_var('DATABASE_PORT'),
    }
}

