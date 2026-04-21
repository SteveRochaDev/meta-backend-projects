# Lab 09: Connecting Django to a MySQL Database

## Introduction
In this lab, the Django project was configured to use a MySQL database instead of the default SQLite database, demonstrating how to work with an external database system.

## Goal
Connect a Django application to a MySQL database.

## Objectives

- Create a MySQL database (`feedback`).
- Configure Django database settings.
- Install and use a MySQL database connector (`mysqlclient`).
- Apply migrations to MySQL.

## Database Configuration

Example `DATABASES` setting in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedback',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

## Commands Used

```powershell
pip install mysqlclient
python manage.py makemigrations
python manage.py migrate
```

## Final Result

- Django successfully connected to MySQL.
- All application tables were created in the MySQL database.
- The project is now ready to scale beyond SQLite.

## Status

Lab completed successfully.

**Grade:** 100%