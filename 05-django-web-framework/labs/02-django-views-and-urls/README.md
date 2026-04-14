# Lab 02: Creating a View and URL Configuration in Django

## Introduction
In this lab, a simple Django web page was created by defining a view and configuring URL routing at both the app and project levels. This allowed a custom HTML response to be displayed in the browser.

## Goal
Build a basic Django web page using views and URL configuration.

## Objectives

- Create a Django view using `HttpResponse`
- Configure app-level URL routing
- Configure project-level URL routing using `include()`
- Register the app in Django settings
- Display a custom webpage in the browser

## Project Structure

- `myapp/views.py` → Contains the view function
- `myapp/urls.py` → Defines app-level routes
- `myproject/urls.py` → Connects app URLs to the project
- `myproject/settings.py` → Registers the Django app

## Key Concepts

- Django views
- URL routing system
- `HttpResponse`
- `path()` and `include()` functions
- Separation of project and app responsibilities

## Commands Used

```bash
python manage.py runserver
```

## Final Result

A working Django web page was successfully created and displayed in the browser at:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

The page renders the message:

> Welcome to Little Lemon!

## Status

Lab completed successfully.

**Grade:** 100%