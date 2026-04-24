# Lab 02: Convert BookList API Project to DRF

## Introduction
In this lab, the existing BookList API project was upgraded from plain Django to Django REST Framework (DRF). Instead of using function-based views and JsonResponse, DRF serializers and generic views were used to build a more robust and scalable API.

## Goal
Convert a basic Django API into a Django REST Framework API.

## Objectives

- Create a Django model for books
- Use DRF serializers to handle data conversion
- Implement class-based API views using DRF generics
- Support GET and POST requests using DRF
- Test API endpoints through the DRF browsable interface

## Project Structure

- `BookList/manage.py` → Django management script
- `BookList/BookList/settings.py` → Project settings
- `BookList/BookList/urls.py` → Project-level URL configuration
- `BookList/BookListDRF/models.py` → Defines the `Book` model
- `BookList/BookListDRF/serializers.py` → Defines the `BookSerializer`
- `BookList/BookListDRF/views.py` → Defines DRF API views
- `BookList/BookListDRF/urls.py` → App-level URL configuration
- `BookList/db.sqlite3` → SQLite database

## Key Concepts

- Django REST Framework (DRF)
- Serializers
- Class-based views
- Generic views (`ListCreateAPIView`, `RetrieveUpdateAPIView`)
- API endpoints
- JSON responses
- GET and POST methods

## API Endpoints

- List & Create Books: [http://127.0.0.1:8000/api/books](http://127.0.0.1:8000/api/books)
- Retrieve / Update Single Book: [http://127.0.0.1:8000/api/books/<id>](http://127.0.0.1:8000/api/books/<id>)

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Final Result

- A `Book` model was created with the fields: `title`, `author`, `price`.
- A DRF serializer (`BookSerializer`) was implemented to convert model data into JSON.
- A class-based API view (`BookView`) was created using `ListCreateAPIView` for listing and adding books.
- A second view (`SingleBookView`) was created using `RetrieveUpdateAPIView` for accessing individual books.
- API endpoints were configured and tested successfully.
- Three books were added through the DRF interface:
  - The Prophet — Kahlil Gibran — 4.35
  - Siddhartha — Hermann Hesse — 8.95
  - The Great Gatsby — Francis Scott Fitzgerald — 6.90

## Status

Lab completed successfully.

**Grade:** 100%