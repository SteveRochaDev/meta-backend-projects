# Lab 07: Working with Forms in Django

## Introduction
In this lab, a Django ModelForm was created to collect user input and store it in the database. This demonstrates how Django handles forms, user input, and data persistence.

## Goal
To create a ModelForm using a model and store form data in the database.

## Objectives

- Create a Django model called `Booking`.
- Create a `ModelForm` based on the model.
- Render the form in a webpage.
- Handle form submission using a view.
- Store submitted data in the database.

## Project Structure

- `myapp/models.py` → Defines the `Booking` model
- `myapp/forms.py` → Contains the `BookingForm`
- `myapp/views.py` → Handles form rendering and submission
- `myapp/templates/booking.html` → Displays the form
- `myapp/admin.py` → Registers the model
- `myapp/migrations/` → Stores migration files
- `db.sqlite3` → SQLite database

## Model Created

Example model added to `myapp/models.py`:

```python
from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_time}"
```

## Form Created

Example ModelForm in `myapp/forms.py`:

```python
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
```

## View Logic

Example view in `myapp/views.py`:

```python
from django.shortcuts import render
from .forms import BookingForm

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})
```

## Template

Example template `myapp/templates/booking.html`:

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

## Commands Used

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Final Result

- A booking form is displayed on the webpage.
- Users can submit reservation details.
- Submitted data is stored in the `myapp_booking` table.
- The `reservation_time` field is automatically populated.

## Status

Lab completed successfully.

**Grade:** 100%