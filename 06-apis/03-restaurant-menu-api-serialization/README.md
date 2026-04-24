# Lab 03: Restaurant Menu API using Serialization

## Introduction
In this lab, a Restaurant Menu API was created using Django REST Framework. A `MenuItem` model was built and exposed through serialized API endpoints that support creating, listing, retrieving, updating, and deleting menu items.

## Goal
Build a restaurant menu API using DRF serialization, validation, and deserialization.

## Objectives

- Create a Django model for restaurant menu items
- Use DRF serializers to convert model data into JSON/XML
- Add validation rules using serializer `extra_kwargs`
- Create class-based API views with DRF generics
- Support GET, POST, PUT, and DELETE requests
- Display API data in JSON and XML formats

## Project Structure

- `LittleLemon/manage.py` → Django management script
- `LittleLemon/LittleLemon/settings.py` → Project settings
- `LittleLemon/LittleLemon/urls.py` → Project-level URL configuration
- `LittleLemon/LittleLemonDRF/models.py` → Defines the `MenuItem` model
- `LittleLemon/LittleLemonDRF/serializers.py` → Defines the `MenuItemSerializer`
- `LittleLemon/LittleLemonDRF/views.py` → Defines DRF API views
- `LittleLemon/LittleLemonDRF/urls.py` → App-level URL configuration
- `LittleLemon/db.sqlite3` → SQLite database

## Key Concepts

- Django REST Framework
- Serializers
- Deserialization
- Validation
- Generic views
- `ListCreateAPIView`
- `RetrieveUpdateDestroyAPIView`
- JSON renderer
- XML renderer
- GET, POST, PUT, and DELETE methods

## API Endpoints

- List & Create Menu Items:  
  [http://127.0.0.1:8000/api/menu-items](http://127.0.0.1:8000/api/menu-items)

- Retrieve, Update & Delete Single Menu Item:  
  [http://127.0.0.1:8000/api/menu-items/{id}](http://127.0.0.1:8000/api/menu-items/{id})

- XML format:  
  [http://127.0.0.1:8000/api/menu-items?format=xml](http://127.0.0.1:8000/api/menu-items?format=xml)

- JSON format:  
  [http://127.0.0.1:8000/api/menu-items?format=json](http://127.0.0.1:8000/api/menu-items?format=json)

## Model Created

Example `MenuItem` model added to `LittleLemon/LittleLemonDRF/models.py`:

```python
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title
```

## Serializer Created

Example serializer in `LittleLemon/LittleLemonDRF/serializers.py`:

```python
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0},
        }
```

## Views Created

Example views in `LittleLemon/LittleLemonDRF/views.py`:

```python
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

## Commands Used

```powershell
pip install djangorestframework-xml
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Final Result

- A `MenuItem` model was created with the fields: `title`, `price`, and `inventory`.
- A DRF serializer was created to serialize and validate menu item data.
- API endpoints were created for listing, creating, retrieving, updating, and deleting menu items.
- Validation was added so:
  - `price` must be at least 2
  - `inventory` must be at least 0
- Menu items were added through the DRF browsable API.
- The API supports JSON and XML output formats.

## Status

Lab completed successfully.

**Grade:** 100%