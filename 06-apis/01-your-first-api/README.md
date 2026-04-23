# Lab 01: Your First API

## Introduction
In this lab, a BookList API project was built using plain Django. A `Book` model was created, registered in the Django admin, and exposed through a function-based API view that supports both GET and POST requests.

## Goal
Build a basic API in Django to list and add books.

## Objectives

- Create a Django model for a database table
- Register the model in the Django admin
- Create a function-based API view
- Use GET and POST methods to interact with the database
- Run the Django development server and test the API output

## Project Structure

- `BookList/manage.py` → Django management script
- `BookList/BookList/settings.py` → Project settings
- `BookList/BookList/urls.py` → Project-level URL configuration
- `BookList/BookListAPI/models.py` → Defines the `Book` model
- `BookList/BookListAPI/views.py` → Defines the API view
- `BookList/BookListAPI/admin.py` → Registers the `Book` model in admin
- `BookList/BookListAPI/urls.py` → App-level URL configuration
- `BookList/db.sqlite3` → SQLite database

## Key Concepts

- Django models
- Django admin
- Function-based views
- `JsonResponse`
- GET and POST methods
- `csrf_exempt`
- `model_to_dict`
- Database migrations

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Final Result

- A `Book` model was created with the fields: `title`, `author`, `price`.
- The model was registered in Django admin.
- Two book entries were added through the admin panel:
  - Northanger Abbey by Jane Austen
  - Siddhartha by Hermann Hesse
- An API endpoint was created at: [http://127.0.0.1:8000/api/books](http://127.0.0.1:8000/api/books)
- A GET request returns the list of books in JSON format.
- A POST request allows adding a new book to the database.

## Status

Lab completed successfully.

**Grade:** 100%