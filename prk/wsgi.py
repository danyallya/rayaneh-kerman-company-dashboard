"""
WSGI config for prk project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/www/prk')
sys.path.append('/www/prk/prk')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prk.settings")

# serve django via WSGI
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
import django

django.setup()
