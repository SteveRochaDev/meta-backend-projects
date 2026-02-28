# Lab 03: Improve Your Bio Page with Bootstrap

## Introduction
This lab focuses on enhancing a biographical page using Bootstrap. You will practice using the Bootstrap Grid and components to make a responsive bio page.

## Goal
Use Bootstrap to build a responsive biographical page with a photo, lists, and a profile button.

## Objectives
- Add a Bootstrap Grid to the page
- Make content responsive on mobile and desktop
- Make the photo responsive using Bootstrap
- Convert the Meta profile link into a Bootstrap button

## Project Structure
- `index.html`
- `photo.jpg`
- `bootstrap.min.css`
- `bootstrap.bundle.min.js`
- `README.md`

## Instructions

### Setting up the Bootstrap Grid
1. Open `index.html`.
2. Add a `container` div.
3. Inside it, add a `row` div.
4. Add two divs inside the row:
    - First div: `id="bio"` and classes `col-12 col-lg-6 text-center`
    - Second div: `id="more"` and classes `col-12 col-lg-6`

### Adding Content
1. Inside the `bio` div:
    - Add an `<h1>` heading with your name
    - Add an `<img>` element for `photo.jpg` with the class `img-fluid`
2. Inside the `more` div:
    - Add `<h2>` heading: `Favorite Music Artists`
    - Add an unordered list `<ul>` of your 5 favorite artists
    - Add `<h2>` heading: `Favorite Films`
    - Add an ordered list `<ol>` of your top 5 films
    - Add an anchor `<a>` linking to your Meta profile:
        ```html
        <a href="https://www.meta.com/" class="btn btn-primary">My Meta Profile</a>
        ```

### Final Steps
1. Save the file
2. Start **Go Live** in VS Code
3. Open browser preview and verify the layout and components
4. Stop the live server once verified

## Key Takeaways
- Bootstrap Grid ensures responsive design
- `.img-fluid` makes images scale correctly
- `.btn` and `.btn-primary` provide consistent button styling

## Status
Lab completed successfully  
**Grade:** 100%