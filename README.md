# Sea-Listings

(*UNDER CONSTRUCTION*)

## Problem Statement

Craigslist has been around the web since 1995. Even though it's one of the most popular marketplace sites for users to peruse for various items, Craigslist's interface has not changed much. The front page interface appears outdated and lacks any visuals besides the user-generated images on listings. This web app hopes to provide images associated with the listings immediately after the user searches for a particular item. In particular, this app will be scraping listings from the Seattle Craigslist site.


## Technologies Used

- Python
- Django
- Bootstrap
- Materialize (front-end framework based on Material Design)
- Beautiful Soup (Python library for web scraping)
- AWS or Heroku

## Getting Started

Create a virtual environment
- Making a virtual environment will allow you to manage package installations for different projects and ensure you will not have any conflicts when creating a new Python application.
- It is HIGHLY recommended that you create a virtual environment before cloning this project

To create a virtual environment 
```bash
virtualenv NAME_OF_ENV
``` 
- Replace NAME_OF_ENV with a name of your choosing

To activate a virtual environment 
```bash
source/bin/NAME_OF_ENV
```
To deactivate, simply write `deactivate`. Make sure when running either of these commands that you are in the same directory as where your virtualenv is located

Check Python and Django versions
- This project was made with Python 3.8.1 and Django 3.0.2
- If you do not have Python installed, follow the directions at this link [Python Download](https://www.python.org/downloads/release/python-381/)
- If you do not have Django installed, run `python -m pip install django`
- Check current Python version with `python --version`
- Check current Django version with `python3 -m django --version`
