#!/usr/bin/env python
from __future__ import absolute_import

import os
import sys

if __name__ == "__main__":

    try:
        import dotenv
        ROOT_DIR = os.path.dirname(__file__)
        dotenv.load_dotenv(os.path.join(ROOT_DIR, ".env"))
    except ImportError:
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
