# Lab 10: Creating Templates in Django

## Introduction
In this lab, Django templates were created for the About and Menu pages of the Little Lemon website. Dynamic content and static files were rendered using Django's template system.

## Goal
Practice using templates in Django.

## Objectives

- Create views for the About and Menu pages
- Create templates for both pages
- Pass dynamic dictionary content to a template
- Display static content such as an image

## Project Structure

- `myproject/settings.py` → Configures template and static file settings
- `myapp/views.py` → Defines About and Menu views using `render()`
- `myapp/urls.py` → Routes requests to the views
- `templates/about.html` → About page template
- `templates/menu.html` → Menu page template
- `myapp/static/img/dessert.jpg` → Static image used in the Menu page

## Key Concepts

- Django templates
- `render()` function
- DTL (Django Template Language)
- Static files
- Passing dictionaries to templates

## Commands Used

```powershell
python manage.py runserver
```

## Final Result

- The About page displays dynamic text passed from a dictionary.
- The Menu page displays a static image using Django static files.
- Both pages are rendered using templates instead of plain `HttpResponse`.

## Status

Lab completed successfully.

**Grade:** 100%