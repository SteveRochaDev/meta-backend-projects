# Lab 13: Design and Build a Simple Django App

## Introduction
In this final assessment, a complete Django application was extended to support a dynamic restaurant menu, individual menu item pages, and shared footer content using template inheritance and partials.

## Goal
Build the Menu page and Menu Item page for the Little Lemon website.

## Objectives

- Create and register the `Menu` model.
- Display menu items dynamically on the Menu page.
- Create a dynamic page for individual menu items.
- Add menu item descriptions.
- Use template links with URL parameters.
- Include a shared footer partial in the base template.

## Project Structure

- `littlelemon/urls.py` → Project-level URL configuration
- `restaurant/urls.py` → App-level URL configuration
- `restaurant/models.py` → Defines `Booking` and `Menu`
- `restaurant/views.py` → Handles all page rendering
- `restaurant/admin.py` → Registers models
- `restaurant/templates/menu.html` → Dynamic menu listing
- `restaurant/templates/menu_item.html` → Single menu item page
- `restaurant/templates/partials/_footer.html` → Shared footer

## Models

Example `Menu` model added to `restaurant/models.py`:

```python
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
```

## Key Features

- Dynamic menu page using model data.
- Dynamic menu item detail page using URL parameter `pk`.
- Footer partial included in `base.html`.
- Admin panel used to manage menu items.
- Booking form remains functional.

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Final Result

- The Menu page displays all menu items from the database.
- Each menu item links to its own detail page.
- Descriptions and images are shown on the menu item page.
- A footer partial is included across the site.

## Status

Lab completed successfully.

**Grade:** 100%