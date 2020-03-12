# Django Polls

## Setup

+ Create virtual environment: `pyton -m venv <environment_name_here>`
+ Install the dependencies: `pip install -r requirements.txt`
+ Edit in your database details in **main/settings.py** under **DATABASES**
+ Run `python manage.py migrate` after setting up the database to create the tables needed.
+ Create a superuser for the project: `python manage.py createsuperuser`
+ Run `python manage.py runserver`
+ Go to "http://localhost:8000" to see the site and "http://localhost:8000/admin" to add poll questions and answers.

