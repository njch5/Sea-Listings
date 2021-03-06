# Sea-Listings

## Problem Statement

Craigslist has been around the web since 1995. Even though it's one of the most popular marketplace sites for users to search for various items, Craigslist's interface has not changed much. The front page interface appears outdated and lacks any visuals besides the user-generated images on listings. This web app hopes to provide an image associated with each listing immediately after the user searches for a particular item and make the app a one-stop search. In particular, this app will be scraping listings from the Seattle Craigslist site.

## Main Features

- Visually pleasing landing page 
- Search for an item based on a keyword
  - User can make queries to find a specific item. When the user hits submit, they are able to view Craigslist postings in real-time
- Filter by pricing
  - User can filter listings from lowest to highest priced items and vice versa
- Filter by location
  - User can filter by zip code and specify the number of miles away from the zip code
- Validation on form
  - Search keyword is required. If user attempts to submit an empty form, they will receive a validation error
  - Zip code input is limited to 5 characters. Both zip code and miles only take numbers.

## Technologies Used

- Python
- Django
- Beautiful Soup (Python library for web scraping)
- JavaScript
- jQuery
- Materialize (front-end framework based on Material Design)
- Heroku

## Video Demo

[![Sea-Listings demo](http://img.youtube.com/vi/V1VeK434Yro/0.jpg)](http://www.youtube.com/watch?v=V1VeK434Yro)

## Getting Started

1.  Create a virtual environment
- Making a virtual environment will allow you to manage package installations for different projects and ensure you will not have any conflicts when creating a new Python application.
- It is HIGHLY recommended that you create a virtual environment before cloning this project

To create a virtual environment 
```bash
virtualenv NAME_OF_ENV
``` 
- Replace NAME_OF_ENV with a name of your choosing

To activate a virtual environment 
```bash
source NAME_OF_ENV/bin/activate
```
To deactivate, simply write `deactivate`. Make sure when running either of these commands that you are in the same directory as where your virtualenv is located

2.  Check Python and Django versions
- This project was made with Python 3.8.1 and Django 3.0.2
- If you do not have Python installed, follow the directions at this link [Python Download](https://www.python.org/downloads/release/python-381/)
- If you do not have Django installed, run `python -m pip install django`
- Check current Python version with `python --version`
- Check current Django version with `python3 -m django --version`

3.  Install dependencies from requirements.txt file
- Run the command `pip install -r requirements.txt` in order to have all the dependencies you need to run the web application

4.  Check dependencies installed with `pip list`
- This is ensure that your dependencies have been installed correctly

5.  Run the web server on your localhost
- In the terminal, run the command `python manage.py runserver`. This must be done in the same directory as where the manage.py file is located.
- Use Google Chrome as the preferred browser
- If the command is successful, the web app can be seen on http://127.0.0.1:8000/

## Biggest Takeaways from Capstone

- This is often said at Ada but needs to be repeated often: DEPLOY EARLY AND DEPLOY OFTEN!
  - I'm glad I took the time to deploy at the end of the week 1 because deployment took over 5 hours after encountering a bizarre set of errors.
  - During my time at Ada, I've learned to not fear the errors I was getting in my terminal but to embrace the challenge of being able to solve the issues.

- Virtual environments are very handy and makes it easy to not have conflicting dependencies across multiple projects.

- There are TONS of libraries that will make your life easier (especially with CSS!!)
