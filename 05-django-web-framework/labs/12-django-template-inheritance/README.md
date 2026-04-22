# Lab 12: Working with Template Inheritance in Django

## Introduction
In this lab, Django template inheritance was used to share common layout elements across multiple pages. A partial template was included for the header and navigation menu.

## Goal
Practice using partial templates and template inheritance in Django.

## Objectives

- Use `include` for partial templates
- Use `extends` for shared layout
- Create a common base template
- Reuse a shared header across multiple pages

## Project Structure

- `templates/base.html` → Main base template
- `templates/index.html` → Home page template
- `templates/about.html` → About page template
- `templates/menu.html` → Menu page template
- `templates/book.html` → Book page template
- `templates/partials/_header.html` → Shared header and navigation
- `myapp/views.py` → Renders the pages
- `myproject/settings.py` → Configures static files

## Key Concepts

- Template inheritance with `extends`
- Partial templates with `include`
- Reusable page layout
- Shared navigation menu
- Static files in templates

## Commands Used

```powershell
python manage.py runserver
```

## Final Result

- All pages share the same header and navigation menu.
- Each page extends `base.html`.
- The header is included from a partial template.
- Template inheritance is successfully implemented.

## Status

Lab completed successfully.

**Grade:** 100%