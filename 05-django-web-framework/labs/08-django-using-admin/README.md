# Lab 08: Using Django Admin

## Introduction
In this lab, the Django admin panel was used to manage models, create users, and assign permissions.

## Goal
To learn how to use Django admin for database management and user administration.

## Objectives

- Create a superuser with admin privileges.
- Create an Employees model.
- Register models in Django admin.
- Add employee records through the admin panel.
- Create users and assign permissions.

## Project Structure

- `myapp/models.py` → Defines Employees model
- `myapp/admin.py` → Registers models
- `db.sqlite3` → Database storing employees and users

## Model Created

Example model added to `myapp/models.py`:

```python
from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

## Admin Registration

Register the model in `myapp/admin.py`:

```python
from django.contrib import admin
from .models import Employees

admin.site.register(Employees)
```

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Admin Actions

- Created superuser: `admin` (example)
- Logged into Django admin panel
- Added employee: Priya Giti
- Created user: `jason_chef`
- Assigned permissions

## Final Result

- Employees managed via Django admin
- Users created and controlled via admin panel
- Permissions successfully assigned

## Status

Lab completed successfully.

**Grade:** 100%