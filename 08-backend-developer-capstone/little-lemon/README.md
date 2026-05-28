# Little Lemon Restaurant - Backend Capstone Project

## Introduction

This project is the Backend Capstone for the Meta Back-End Developer Professional Certificate. It provides a REST API for the Little Lemon restaurant built with Django and Django REST Framework.

## Features Implemented

- Django project with MySQL (or SQLite) database support
- Menu management API
- Table booking API
- Token authentication using Djoser
- Static HTML pages served by Django for basic UI
- Unit tests for APIs
- Clear project structure and documentation

## Project Structure

```text
little-lemon/
├── littlelemon/             # Main Django project
├── menu/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── tests.py
│   └── urls.py (if exists)
├── bookings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── tests.py
├── templates/               # Static HTML pages
├── manage.py
├── requirements.txt
├── README.md
└── README.txt
```

## API Endpoints

### HTML Pages (Static Content)

- `GET /` → Home page
- `GET /about/` → About page
- `GET /menu/` → Menu page
- `GET /book/` → Book a table page

### REST API

- `GET /api/menu/` → List all menu items
- `POST /api/menu/` → Create a new menu item (requires manager/admin)
- `GET /api/bookings/` → List bookings
- `POST /api/bookings/` → Create a booking

### Authentication

- `POST /api/auth/token/login/` → Login and obtain authentication token

## How to Test (development)

Run these commands to set up and start the development server:

```bash
pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

After the server is running, obtain a token by POSTing credentials to `/api/auth/token/login/` (example):

- Username: `admin`
- Password: `Root123!?` (example - replace with your admin password)

Use the token in request headers:

```
Authorization: Token <your-token>
```

## Technologies Used

- Django 6.x
- Django REST Framework
- MySQL (or SQLite for local development)
- Djoser (authentication)
- Python 3.11+ (adjust as needed)

## Status

Project completed successfully. Ready for peer review and submission.