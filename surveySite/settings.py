# Django settings for example_app project.
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_ROOT,'dev.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

"""
Follow these directions to build the documentation using Sphinx. Then the
example app will serve the documentation.

1. Install Sphinx. For example,
   $ pip install sphinx
2. Build the documentation using Sphinx.
   $ cd django-crowdsourcing/docs
   $ sphinx-build -b html . _build
"""
DOCUMENTATION_ROOT = os.path.join(PROJECT_ROOT, '../docs/_build')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%n@##5o0%d@qd5l4^+(zt5ih@90a7ch4k3m7a^!5unw45)i=ly'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'surveySite.middleware.RequireLoginMiddleware',  
)


LOGIN_REQUIRED_URLS = (
    r'/crowdsourcing/(.*)$',
    # r'/(.*)$',
    )

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/login(.*)$',
        r'/complete(.*)$',
        r'/associate(.*)$',
        r'/disconnect(.*)$',
        r'/admin(.*)$',
    )

ROOT_URLCONF = 'surveySite.urls'

DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates')
)

FACEBOOK_APP_ID              = '701221253237127'
FACEBOOK_API_SECRET          = '3918ee9a832afc4e141186930c408b3a'

#LOGIN_URL = '/login/facebook/?next=/'
LOGIN_URL = '/login/facebook/'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'social_auth',
    'crowdsourcing',
    'cms',
)

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/newUser' 

try:
    from local_settings import *
except ImportError:
    pass
