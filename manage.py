#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from environs import Env


def main():
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    base_dir = Path(__file__).resolve().parent
    # Reading environment variables
    env = Env()
    env.read_env(os.path.join(base_dir, ".env"), recurse=False)

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env.str("DJANGO_SETTINGS_MODULE"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
