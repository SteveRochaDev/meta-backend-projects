# Lab 03: Mapping URLs with Parameters in Django

## Introduction
In this lab, a Django web page was created using dynamic URL routing. URL parameters were captured using path converters and used inside a view function to display dynamic content.

---

## Goal
Learn how to use Django URL parameters to pass values from the URL into a view function.

---

## Objectives
- Create dynamic URL patterns using path converters
- Capture URL parameters in a Django view
- Use dictionaries to map URL values to content
- Return dynamic HTTP responses using `HttpResponse`

---

## Project Structure
- `myapp/views.py` → Contains the view function with URL parameter handling
- `myapp/urls.py` → Defines dynamic URL routes using `<str:drink_name>`
- `myproject/urls.py` → Connects app URLs to the project
- `myproject/settings.py` → Registers the Django app

---

## Key Concepts
- Dynamic URL routing in Django
- Path converters (`<str:...>`)
- View functions with parameters
- Dictionary-based lookup
- `HttpResponse`

---

## URLs Tested
The following URLs were tested successfully:

- http://127.0.0.1:8000/drinks/mocha/
- http://127.0.0.1:8000/drinks/tea/
- http://127.0.0.1:8000/drinks/lemonade/

Each URL returns a different response based on the parameter provided.

---

## Example Output

For `/drinks/mocha/`:

mocha  
type of coffee

---

## Status
Lab completed successfully.  
**Grade:** 100%