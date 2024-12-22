#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joblisting_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. "
            "Did you forget to activate your virtual environment?"
        ) from exc

    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"An error occurred while executing the command: {e}")        
        sys.exit(1)


if __name__ == '__main__':
    main()
