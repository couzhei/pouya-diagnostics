import os

import environ

from .base import *

env = environ.Env()
environ.Env.read_env()

DEBUG = False

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
]
# ALLOWED_HOSTS is a list of strings that represent the host/domain names
# that your project can serve. This is a security measure to prevent an
# attacker from poisoning caches and DNS. Find more details about
# ALLOWED_HOSTS in the Django documentation.


DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": env("POSTGRES_NAME", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": env("POSTGRES_USER", default="user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="password"),
        "HOST": env("POSTGRES_URL", default="localhost"),
        "PORT": env("POSTGRES_PORT", default=""),
    }
}

SECURE_SSL_REDIRECT = True
# SECURE_SSL_REDIRECT redirects all HTTP requests to HTTPS (unless exempt).
# This means your project will always try to use an encrypted connection.
# You will need to have SSL configured on your server for this to work.
# Note that if you have Nginx or Apache configured to do this already,
# this setting will be redundant.

SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE tells the browser that cookies can only be handled
# over HTTPS. This means cookies your project produces for activities,
# such as logins, will only work over an encrypted connection.

CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE is the same as SESSION_COOKIE_SECURE but applies
# to your CSRF token. CSRF tokens protect against cross-site request
# forgery. Django CSRF protection does this by ensuring any forms submitted
# (for logins, signups, and so on) to your project were created by your
# project and not a third party.

SECURE_BROWSER_XSS_FILTER = True
# SECURE_BROWSER_XSS_FILTER sets the X-XSS-Protection: 1;
# mode=block header on all responses that do not already
# have it. This ensures third parties cannot inject
# scripts into your project. For example, if a user
# stores a script in your database using a public
# field, when that script is retrieved and displayed
# to other users it will not run.
