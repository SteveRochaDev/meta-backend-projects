# Peer-Graded Assignment: Little Lemon Booking System

## Introduction

In this project, a complete booking system for the Little Lemon restaurant was developed using Django, Django REST Framework, JavaScript, and the Fetch API. Customers can create reservations through a booking form while the system dynamically checks booked time slots and prevents duplicate reservations.

The project was created as part of the Meta Back-End Developer Professional Certificate.

---

## Goal

Build a full-stack restaurant booking system with a Django backend, REST API, dynamic frontend interactions, and booking validation.

---

## Objectives

- Create a Django project and restaurant app
- Build a booking model using Django ORM
- Create REST API endpoints using Django REST Framework
- Display bookings as JSON data
- Prevent duplicate bookings for the same date and time
- Create a booking form using HTML
- Use JavaScript Fetch API to retrieve booking data
- Dynamically disable already booked slots
- Automatically select the current date
- Display a “No bookings” message when applicable

---

## Project Structure

- `littlelemon/manage.py` → Django management script
- `littlelemon/littlelemon/settings.py` → Project settings
- `littlelemon/littlelemon/urls.py` → Project-level URL configuration
- `littlelemon/restaurant/models.py` → Defines the Booking model
- `littlelemon/restaurant/views.py` → Defines booking views and API logic
- `littlelemon/restaurant/serializers.py` → Defines the Booking serializer
- `littlelemon/restaurant/urls.py` → App-level URL configuration
- `littlelemon/restaurant/templates/book.html` → Booking form template
- `littlelemon/restaurant/static/script.js` → JavaScript Fetch API logic
- `littlelemon/db.sqlite3` → SQLite database (include in submission)

---

## Key Concepts

- Django
- Django REST Framework
- REST APIs
- Serializers
- Generic API Views
- JavaScript
- Fetch API
- Dynamic Forms
- Booking Validation
- Duplicate Prevention
- JSON Responses

---

## Features Implemented

### Booking Form

- First Name field
- Reservation Date field
- Reservation Slot field

### Dynamic Booking System

- Current date selected automatically
- Existing bookings retrieved dynamically using Fetch API
- Booked slots displayed as unavailable
- Duplicate reservations prevented

### Booking API

- List all bookings
- Create bookings
- Filter bookings by date

---

## API Endpoint

### List & Create Bookings

```text
GET/POST http://127.0.0.1:8000/bookings/
```

### Filter Bookings by Date

```text
GET http://127.0.0.1:8000/bookings/?date=2026-05-26
```

### Booking Form Page

```text
GET http://127.0.0.1:8000/book/
```

---

## Example Booking Model

Example model defined in `restaurant/models.py`:

```python
from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField()

    def __str__(self):
        return f"{self.first_name} on {self.reservation_date} slot {self.reservation_slot}"
```

## Example API View

Example API view defined in `restaurant/views.py`:

```python
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(generics.ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        date = self.request.query_params.get('date')
        if date:
            queryset = queryset.filter(reservation_date=date)
        return queryset
```

---

## Commands Used (development)

```powershell
pipenv install django djangorestframework
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Final Result

- A booking system was created using Django and DRF.
- Reservations can be created through the booking form.
- Existing bookings are retrieved dynamically using Fetch API.
- Duplicate bookings for the same date and slot are prevented.
- Booked slots are automatically disabled in the form.
- Bookings can be filtered by date through the API.
- A “No bookings” message is displayed when no reservations exist for a selected date.

## Status

Project completed successfully.

Assignment ready for submission.