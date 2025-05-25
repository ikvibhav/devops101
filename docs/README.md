# Tech Stack and Definitions

## Django
1. Files - 
    1. asgi.py and wsgi.py - Allows to communicate with the folder
    2. settings.py - Go here when trying to install various django applications settings
    3. urls.py - Used to route various URLs to different routes
    4. manage.py - Manage application, create database server, manage URLS etc
2. Apps -
    1. In django, app is a modular component of project responsible for a specific piece of functionality
3. ORM (Object Relational Mapping) -
    1. ORM in python refers to a programming technique that iteracts with relational databases (PostGreSQL, MySQL etc)
    and representing database tables as python classes and rows as python objects
4. Migrations
    1. Migrations are ways to propogate changes made in models (Python classes represnting DB tables) into database schemas
5. Useful Commands -
    To start new project -
    ```
    django-admin startproject <PROJECT_NAME>
    ```

    To create a new app -
    ```
    python manage.py startapp <APP_NAME>
    ```

    To run a django server -
    ```
    python manage.py runserver
    ```

    To make django migrations. Fromproject directory -
    ```
    python manage.py makemigrations
    ```

    To apply django migrations. Fromproject directory -
    ```
    python manage.py migrate
    ```

    To create django users -
    ```
    python manage.py createsuperuser
    ```