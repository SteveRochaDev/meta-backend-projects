# Lab 04: Creating URLs and Mapping to Views in Django

## Introduction
In this lab, multiple views were created in a Django application and mapped to different URL paths. This allowed the website to display different pages depending on the route accessed in the browser.

## Goal
Create multiple views and configure URL routing to display different pages in a Django web application.

## Objectives
- Create multiple view functions inside `views.py`
- Map each view to a specific URL path
- Configure app-level URL routing using `path()`
- Understand how Django routes requests to views

## Project Structure
- `myapp/views.py` → Contains all view functions
- `myapp/urls.py` → Maps URLs to views
- `myproject/urls.py` → Includes app-level URLs in the project

## Views Created
- `home` → Displays "Welcome to Little Lemon!"
- `about` → Displays "About us"
- `menu` → Displays "Menu"
- `book` → Displays "Make a booking"

## URL Mapping
- `/` → Home page
- `/about/` → About page
- `/menu/` → Menu page
- `/book/` → Booking page

## Key Concepts
- Django views
- URL dispatcher
- URL routing with `path()`
- Mapping multiple views in a single app

## Final Result
A Django web application with four working pages:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/about/
- http://127.0.0.1:8000/menu/
- http://127.0.0.1:8000/book/

Each URL correctly renders its corresponding view in the browser.

## Status
Lab completed successfully.  
**Grade:** 100%