# Lab 01: Creating your first Django project

## Introduction
This lab introduces the setup of a Django project using a Python virtual environment. You will create a Django project, configure a Django app, and run a local development server.

## Goal
Set up a Django project inside a virtual environment and successfully run the Django development server.

## Objectives

- Create a Python virtual environment.
- Activate the virtual environment.
- Install Django using pip.
- Create a Django project using `django-admin startproject`.
- Create a Django application using `python manage.py startapp`.
- Register the application in `settings.py`.
- Apply database migrations.
- Run the Django development server.

## Project Structure

- `django-venv/`
- `myproject/`
  - `manage.py`
  - `myproject/`
  - `myapp/`
  - `db.sqlite3`
- `README.md`

## Instructions

### Virtual Environment Setup

1. Create a virtual environment:

   ```powershell
   python -m venv django-venv
   ```

1. Activate the virtual environment (PowerShell):

   ```powershell
   .\django-venv\Scripts\Activate
   ```

### Install Django

1. Install Django using pip:

   ```powershell
   pip install django
   ```

### Create Django Project

1. Create a Django project:

   ```powershell
   django-admin startproject myproject
   ```

1. Navigate into the project directory:

   ```powershell
   cd myproject
   ```

### Create Django App

1. Create a Django app:

   ```powershell
   python manage.py startapp myapp
   ```

1. Add `myapp` to `INSTALLED_APPS` inside `myproject/settings.py`.

### Database Setup

1. Apply migrations:

   ```powershell
   python manage.py migrate
   ```

### Run Server

1. Start the development server:

   ```powershell
   python manage.py runserver
   ```

1. Open the browser and visit the development server URL:

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Key Takeaways

- Django projects typically use a virtual environment for dependency isolation.
- `django-admin startproject` creates the main project structure.
- `python manage.py startapp` creates a modular application within the project.
- Apps must be registered in `INSTALLED_APPS`.
- Migrations initialize the database structure.
- The development server is intended for local testing only.

## Status

Lab completed successfully.

**Grade:** 100%