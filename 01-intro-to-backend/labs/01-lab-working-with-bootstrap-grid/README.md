# Lab 01: Working with Bootstrap Grid

## Introduction
This lab focuses on building a responsive webpage using the Bootstrap Grid system. You will practice creating rows and columns to display content in a structured, mobile-friendly layout.

## Goal
Create a two-column food menu for Little Lemon with the logo centered at the top.

## Objectives
- Set up a Bootstrap container  
- Display the Little Lemon logo in the top center using Bootstrap  
- Create a responsive two-column menu layout using the Bootstrap Grid  

## Project Structure
- `index.html`  
- `logo.png`  
- `bootstrap.min.css`  
- `bootstrap.bundle.min.js`  
- `README.md`  

## Instructions

### HTML Structure
1. Open `index.html`.  
2. Create a `<div>` with the class `container` inside the `<body>`.  
3. Add three `<div>` elements with class `row` inside the container.  

**First row – Logo**
4. Add a `<div>` with class `col-12` inside the first row.  
5. Inside this, add a `<div>` with class `text-center`.  
6. Place an `<img>` element for `logo.png` with class `img-fluid`.  

**Second row – Page Title**
7. Add a `<div>` with class `col-12` inside the second row.  
8. Inside this, add a `<div>` with class `text-center`.  
9. Place an `<h1>` element with text: `Our Menu`.  

**Third row – Two-column menu**
10. Add two `<div>` elements inside the third row with class `col-12 col-lg-6`.  

**First column**
- `<h2>`: `Falafel`  
- `<p>`: `Chickpea, herbs, spices`  
- `<h2>`: `Fried Calamari`  
- `<p>`: `Squid, buttermilk`  

**Second column**
- `<h2>`: `Pasta Salad`  
- `<p>`: `Lettuce, vegetables, mozzarella`  
- `<h2>`: `Greek Salad`  
- `<p>`: `Cucumbers, onion, feta cheese`  

### Final Steps
1. Save `index.html`.  
2. Start **Go Live** in VS Code to preview your page.  
3. Use browser preview and select the Macbook 15 device to check responsiveness.  
4. Verify that the menu displays correctly in two columns on larger screens.  
5. Stop the live server once complete.  

## Key Takeaways
- Bootstrap Grid uses a 12-column layout for responsive design.  
- `col-12` spans the full width, while `col-lg-6` spans half on large screens.  
- `.container` and `.row` are essential building blocks for layout.  
- `.text-center` and `.img-fluid` help with alignment and responsiveness.  

## Status
Lab completed successfully.  
**Grade:** 100%