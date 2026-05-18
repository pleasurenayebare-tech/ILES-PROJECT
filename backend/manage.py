#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
   This is the entry point for Django management commands such as :
    -runserver  : Start the development server
    -makemigrations/migrate : Handle database migrations
    -createsuperuser : Create an admin user
    -shell        : Open an interactive Python shell with Django loaded 

   Usage:
     python manage.py <command> [options]
   """
   
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
  #Import Django's CLI execution function 
        from django.core.management import execute_from_command_line
    except ImportError as exc:
  #Raised when Django is not installed or the virtual environment is not activated. Make sure to run: pip install -r requirements.txt
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
   #Pass command-line arguments to Django's management command handler
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    #Only runs when the script is executed directly(not when imported)
    main()
