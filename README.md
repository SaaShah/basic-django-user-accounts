# basic-django-user-accounts
A sample project using basic django-user-accounts with my personal-django-base.

- Python 2.7
- Django 1.7
- SQLite3

# Err101 - Connection Refused

python -m smtpd -n -c DebuggingServer localhost:1025

Use this for a development debugging server.

settings.py

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025
