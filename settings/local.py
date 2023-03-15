from .base import *
import pymysql
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

pymysql.version_info = (1, 4, 2, 'final', 0)
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': 3306
    }
}
