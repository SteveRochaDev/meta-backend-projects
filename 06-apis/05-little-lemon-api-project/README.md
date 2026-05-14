# Little Lemon API Project

## Introduction

In this project, a complete REST API for the Little Lemon restaurant was developed using Django, Django REST Framework, and Djoser. The API supports authentication, role-based permissions, menu management, cart functionality, and order management.

The project was created as part of the Meta Back-End Developer Professional Certificate.

---

## Goal

Build a fully functional REST API for the Little Lemon restaurant with authentication, authorization, filtering, pagination, and ordering features.

---

## Objectives

- Create authentication using Djoser and Token Authentication
- Create role-based permissions for Admins, Managers, Delivery Crew, and Customers
- Create categories and menu items
- Add filtering, searching, ordering, and pagination
- Implement cart functionality
- Implement order management
- Allow managers to assign delivery crew members
- Allow customers to place and browse their orders
- Display API results using the DRF browsable API

---

## Project Structure

- `LittleLemon/manage.py` → Django management script
- `LittleLemon/LittleLemon/settings.py` → Project settings
- `LittleLemon/LittleLemon/urls.py` → Project-level URL configuration
- `LittleLemon/LittleLemonAPI/models.py` → Defines all database models
- `LittleLemon/LittleLemonAPI/views.py` → Defines API views and business logic
- `LittleLemon/LittleLemonAPI/serializers.py` → Defines serializers
- `LittleLemon/LittleLemonAPI/permissions.py` → Defines custom permissions
- `LittleLemon/LittleLemonAPI/urls.py` → App-level URL configuration
- `LittleLemon/db.sqlite3` → SQLite database (include in submission)
- `LittleLemon/notes.txt` → Usernames and passwords for testing (include in submission)

---

## Key Concepts

- Django REST Framework
- Token Authentication
- Djoser Authentication
- Role-Based Permissions
- Pagination
- Ordering
- Searching
- Generic API Views
- Nested Serializers
- Foreign Key Relationships
- REST APIs

---

## User Roles

### Admin

- Assign users to the Manager group
- Add categories
- Add menu items

### Manager

- Log in and obtain authentication tokens
- Assign users to the Delivery Crew group
- Assign orders to delivery crew members
- Update menu items

### Delivery Crew

- Access assigned orders
- Update order delivery status

### Customer

- Register accounts
- Log in and obtain authentication tokens
- Browse menu items and categories
- Add items to cart
- Place orders
- Browse personal orders

---

## API Endpoints

### Authentication (Djoser)

- Register: `POST /auth/users/`
- Login (token): `POST /auth/token/login/`  → returns token

### Categories

- List & Create: `GET/POST /api/categories`

### Menu Items

- List & Create: `GET/POST /api/menu-items`
- Retrieve / Update / Delete single item: `GET/PUT/PATCH/DELETE /api/menu-items/{id}`

### Cart

- List & Create cart items: `GET/POST /api/cart/menu-items`

### Orders

- List & Create orders: `GET/POST /api/orders`
- Retrieve / Update single order: `GET/PUT/PATCH /api/orders/{id}`

### Group management

- Manager group users: `GET/POST /api/groups/manager/users`  (add user to Manager)
- Delivery crew group users: `GET/POST /api/groups/delivery-crew/users`  (add user to Delivery crew)

### Filtering / Ordering / Searching examples

- Order menu items by price: `/api/menu-items?ordering=price`
- Order by descending price: `/api/menu-items?ordering=-price`
- Search menu items by category title: `/api/menu-items?search=starters`
- Pagination: `/api/menu-items?page=2`

---

## Models Created

Example models are defined in `LittleLemon/LittleLemonAPI/models.py` (Category, MenuItem, Cart, Order, OrderItem).

---

## Test Users (included in notes.txt)

| Role           | Username | Password               |
| -------------- | -------- | ---------------------- |
| Admin          | admin    | ThisIsAPassword123!    |
| Manager        | manager  | ThisIsAPassword123!    |
| Delivery Crew  | delivery | ThisIsAPassword123!    |
| Customer       | customer | ThisIsAPassword123!    |

---

## Final Result

- Authentication implemented using Djoser and Token Authentication.
- Role-based permissions implemented for Managers and Delivery Crew (plus admin staff).
- Categories and menu items can be created and browsed via the API.
- Menu items support pagination, ordering, and searching.
- Customers can manage carts and place orders.
- Delivery crew members can access and update assigned orders.
- Managers can manage users and assign orders.
- The DRF browsable API is configured for easy testing.

## Status

Project completed successfully.

Assignment ready for submission.