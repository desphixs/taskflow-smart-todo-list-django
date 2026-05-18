#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# We import the standard 'os' (operating system) module to interact with our computer's system paths and environment settings.
import os
# We import the standard 'sys' (system) module to read any commands or arguments typed into the terminal.
import sys


def main():
    """Run administrative tasks."""
    # We set 'taskflow_project.settings' as our default configurations module.
    # Think of this like pointing a universal remote control at the correct TV: it tells Django
    # exactly which settings file to read so it knows how to connect the database and load apps!
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskflow_project.settings')
    try:
        # We try to import Django's execute utility.
        # This is the core engine function that reads what we typed in the terminal
        # (like 'runserver' or 'migrate') and translates it into direct actions!
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or the virtual environment is not activated, Python throws an ImportError.
        # Think of this like turning the key in a car's ignition when the engine has been completely removed!
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # We pass the list of command-line arguments (sys.argv) directly to the execute utility.
    # This executes the command we entered in the command line (e.g. running the server).
    execute_from_command_line(sys.argv)


# This special Python condition checks if this script is being run directly in the terminal
# (e.g. running 'python manage.py'), rather than being imported as a helper library inside another file.
if __name__ == '__main__':
    # If run directly, run the main function to boot up the administrative utility.
    main()

