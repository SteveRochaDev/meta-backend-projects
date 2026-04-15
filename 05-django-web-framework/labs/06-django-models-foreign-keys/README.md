# Lab 06: Models Using Foreign Keys in Django

## Introduction
In this lab, two Django models were created and linked using a Foreign Key relationship to represent a one-to-many relationship between drink categories and drinks.

## Goal
To create related models using Foreign Keys and apply migrations in Django.

## Objectives

- Create a model called `DrinksCategory`.
- Create a model called `Drinks`.
- Establish a one-to-many relationship using `ForeignKey`.
- Perform database migrations.
- Insert data using the Django shell.

## Project Structure

- `myapp/models.py` → Defines models and relationships
- `myapp/admin.py` → Registers models in Django admin
- `myapp/migrations/` → Stores migration files
- `db.sqlite3` → SQLite database file

## Models Created

Example models added to `myapp/models.py`:

```python
from django.db import models

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        DrinksCategory,
        on_delete=models.PROTECT,
        default=None
    )

    def __str__(self):
        return f"{self.drink} - {self.price}"
```

## Admin Registration

Register the models in `myapp/admin.py`:

```python
from django.contrib import admin
from .models import Drinks, DrinksCategory

admin.site.register(Drinks)
admin.site.register(DrinksCategory)
```

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

## Example Shell Commands

```python
from myapp.models import DrinksCategory, Drinks

cat = DrinksCategory(category_name='coffee')
cat.save()

fk = DrinksCategory.objects.get(pk=1)

drink = Drinks(drink='mocha', price=7, category_id=fk)
drink.save()
```

## Final Result

- Two related tables were created in the database.
- A foreign key relationship was successfully implemented.
- Data was inserted using the Django shell.

## Status

Lab completed successfully.

**Grade:** 100%