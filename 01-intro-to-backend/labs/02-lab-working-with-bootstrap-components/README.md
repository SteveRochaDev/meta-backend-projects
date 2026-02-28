# Lab 02: Working with Bootstrap Components

## Introduction
This lab focuses on enhancing a webpage using Bootstrap components. You will practice adding Alerts, Badges, and Buttons to the Little Lemon website.

## Goal
Update the Little Lemon menu webpage to notify customers about new dishes and restaurant updates using Bootstrap components.

## Objectives
- Add a Badge component to indicate a new dish
- Add an Alert component to notify about a restaurant closure
- Add a Button component for online ordering

## Project Structure
- `index.html`
- `logo.png`
- `bootstrap.min.css`
- `bootstrap.bundle.min.js`
- `README.md`

## Instructions

### Adding Components
1. Open `index.html`.
2. Add an alert below the "Our Menu" heading. Example:

    ```html
    <div class="alert alert-info" role="alert">
        Our restaurant will be closed on New Year's Day
    </div>
    ```

3. Add a badge to the Falafel `h2` heading. Example:

    ```html
    <h2>Falafel <span class="badge bg-secondary">New</span></h2>
    ```

4. Add an "Order Online" button below the menu. Example:

    ```html
    <div class="text-center">
        <button type="button" class="btn btn-primary">Order Online</button>
    </div>
    ```

### Final Steps

1. Save the file.
2. Start **Go Live** in VS Code.
3. Open browser preview and check the alert, badge, and button.
4. Stop the live server once verified.

## Key Takeaways

- Bootstrap components allow you to add interactive and styled elements quickly.
- `.alert`, `.badge`, and `.btn` classes provide consistent styling.
- Combining components with the Bootstrap Grid maintains a responsive layout.

## Status

Lab completed successfully.
**Grade:** 100%