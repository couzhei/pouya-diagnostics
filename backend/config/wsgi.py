"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

import environ

environ.Env.read_env()
# The code you’ve added to both this and manage.py does two things.
# First, whenever Django runs — manage.py for running development, wsgi.py
# for production — you’re telling it to look for your .env file. If the file
# exists, you instruct Django to use the settings file that .env recommends;
# otherwise, you use the development configuration by default.
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

application = get_wsgi_application()
