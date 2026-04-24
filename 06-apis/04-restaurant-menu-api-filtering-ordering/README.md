# Lab 04: Restaurant Menu API Filtering and Ordering

## Introduction
In this lab, pagination, ordering, and searching were added to a Restaurant Menu API using Django REST Framework. Two related models were created: `Category` and `MenuItem`, where each menu item belongs to a category.

## Goal
Add pagination, ordering, and searching functionality to a DRF API.

## Objectives

- Create related models using a foreign key
- Serialize nested category data
- Add pagination to API responses
- Add ordering options for menu items
- Add search functionality
- Display API results using the DRF browsable interface

## Project Structure

- `LittleLemon/manage.py` → Django management script
- `LittleLemon/LittleLemon/settings.py` → Project settings
- `LittleLemon/LittleLemon/urls.py` → Project-level URL configuration
- `LittleLemon/LittleLemonDRF/models.py` → Defines the `Category` and `MenuItem` models
- `LittleLemon/LittleLemonDRF/serializers.py` → Defines serializers for categories and menu items
- `LittleLemon/LittleLemonDRF/views.py` → Defines DRF generic views
- `LittleLemon/LittleLemonDRF/urls.py` → App-level URL configuration
- `LittleLemon/db.sqlite3` → SQLite database

## Key Concepts

- Django REST Framework
- Model relationships
- Foreign keys
- Nested serializers
- Pagination
- Ordering
- Searching
- DRF browsable API
- `ListCreateAPIView`

## API Endpoints

- List & Create Categories:  
  `http://127.0.0.1:8000/api/category`

- List & Create Menu Items:  
  `http://127.0.0.1:8000/api/menu-items`

- Order menu items by price:  
  `http://127.0.0.1:8000/api/menu-items?ordering=price`

- Order menu items by inventory descending:  
  `http://127.0.0.1:8000/api/menu-items?ordering=-inventory`

- Search menu items by category title:  
  `http://127.0.0.1:8000/api/menu-items?search=Desserts`

## Models Created

Example models added to `LittleLemon/LittleLemonDRF/models.py`:

```python
from django.db import models

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title
```

## Serializers Created

Example serializers in `LittleLemon/LittleLemonDRF/serializers.py`:

```python
from rest_framework import serializers
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id']
```

## Views Created

Example views in `LittleLemon/LittleLemonDRF/views.py`:

```python
from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['category__title']
```

## DRF Settings

Add the following to your `settings.py` under `REST_FRAMEWORK`:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,
}
```

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Final Result

- A `Category` model and a `MenuItem` model were created.
- A many-to-one relationship was created between menu items and categories.
- Menu items can be listed and created through the DRF browsable API.
- Category data is displayed as nested serialized data.
- API pagination was configured.
- Menu items can be ordered by price and inventory.
- Menu items can be searched by category title.

## Status

Lab completed successfully.

**Grade:** 100%