# Wiki — Django Encyclopedia

A Wikipedia-style encyclopedia built with Django for **CS50's Web Programming with Python and JavaScript (CS50W)**.

Entries are stored as Markdown files and rendered as HTML. Users can browse articles, search by title, create and edit entries, and navigate to a random page.

## Features

- Browse encyclopedia entries
- Render Markdown articles as HTML
- Case-insensitive search with exact and partial matching
- Create new entries
- Edit existing entries
- Prevent duplicate titles
- Open a random article

## Tech Stack

- Python
- Django
- HTML / CSS
- Bootstrap
- `markdown2`

## Running Locally

```bash
pip install Django==3.0.2 markdown2
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Implementation

Encyclopedia articles are stored as individual `.md` files. Django views handle routing, search, creation and editing, while `markdown2` converts Markdown content into HTML for display.

## Attribution

Built for **CS50W Project 1: Wiki**.

CS50 provided the initial Django project structure, helper functions, interface scaffolding, and sample entries. I implemented the application's encyclopedia functionality, including page rendering, search, creation/editing, random-page navigation, and Markdown conversion.

Project specification:  
https://cs50.harvard.edu/web/projects/1/wiki/
