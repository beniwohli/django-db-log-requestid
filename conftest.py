#!/usr/bin/env python
import sys
import os

from os.path import abspath, dirname

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
ROOT_DIR = dirname(abspath(__file__))

sys.path.insert(0, ROOT_DIR)

# don't run tests of dependencies that land in "build" and "src"
collect_ignore = ['build', 'src']


try:
    from psycopg2cffi import compat
    compat.register()
except ImportError:
    pass


def pytest_configure(config):
    from django.conf import settings
    if not settings.configured:
        import django
        if hasattr(django, 'setup'):
            django.setup()