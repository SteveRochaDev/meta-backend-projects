# Lab 01: Create a Grid Layout

## Introduction

In this lab, a responsive Holy Grail layout was created using CSS Grid. The layout includes a header, footer, main content area, and two sidebars. CSS Grid and media queries were used to create a responsive webpage structure for different screen sizes.

## Goal

Create a responsive grid layout using CSS Grid and the `grid-template-areas` property.

## Objectives

- Create a grid layout using CSS Grid
- Define grid template areas
- Configure rows and columns within the grid
- Add responsive behavior using media queries
- Create a Holy Grail webpage layout

## Project Structure

- `index.html` → Defines the webpage structure
- `styles.css` → Defines the CSS Grid layout and responsive styling

## Key Concepts

- CSS Grid
- Grid Template Areas
- Grid Columns
- Grid Rows
- Responsive Design
- Media Queries
- Holy Grail Layout

## Layout Structure

### Small Screens

The layout uses a single-column structure:

- Header
- Left Sidebar
- Main Content
- Right Sidebar
- Footer

### Large Screens (440px and wider)

The layout changes into a three-column grid:

- Header spans all columns
- Left Sidebar | Main Content | Right Sidebar
- Footer spans all columns

## CSS Rules Added

Example grid configuration added to `styles.css`:

```css
.container {
    display: grid;
    max-width: 900px;
    min-height: 50vh;
    grid-template-columns: 100%;
    grid-template-rows: auto auto 1fr auto auto;
    grid-template-areas:
        "header"
        "left"
        "main"
        "right"
        "footer";
}

@media (min-width: 440px) {
    .container {
        grid-template-columns: 150px 1fr 150px;
        grid-template-rows: auto 1fr auto;
        grid-template-areas:
            "header header header"
            "left main right"
            "footer footer footer";
    }
}
```

## Commands Used

```powershell
Go Live
```

## Final Result

- A responsive Holy Grail layout was created using CSS Grid.
- Grid template areas were used to organize page sections.
- Media queries were added for responsive behavior.
- The webpage dynamically adapts to different screen sizes.

## Status

Lab completed successfully.

**Grade:** 100%