"""
WSGI config for primera_aplicaion_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
# por defecto usar este archivo

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primera_aplicaion_django.settings')

application = get_wsgi_application()
