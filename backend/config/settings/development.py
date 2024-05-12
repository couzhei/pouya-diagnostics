import os

import environ  # this is not used for development really

from .base import *

env = environ.Env()  # this is not used for development really
environ.Env.read_env()  # this is not used for development really

# First, you will import from base.py — this
# file inherits settings from base.py. Then
# you’ll transfer the settings you want to
# modify for the development environment.
# In this case, the settings specific to
# development are as follows: DEBUG, which
# you need to be True in development, but
# not in production; and DATABASES, a local
# database instead of a production database.
# You’re using an SQLite database here for
# development.

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        # or
        # "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES = {  # this is not used for development really or why not?
    "default": {
        "ENGINE": env("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": env("POSTGRES_NAME", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": env("POSTGRES_USER", default="user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="password"),
        "HOST": env("POSTGRES_URL", default="localhost"),
        "PORT": env("POSTGRES_PORT", default=""),
    }
}

CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
