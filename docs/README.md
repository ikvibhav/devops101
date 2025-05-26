# Tech Stack and Definitions

## Filesystem Hierarchy Standard (FHS)
1. A set of guildlines that define the organization of directories and files 
on Unix-like operating systems like Linux
    1. bin - system binary
    2. etc - configuration files
    3. var - variable data
    4. home - user home directories
    5. root - root user's home
    6. tmp - temporary files
    7. lib - libraries
    8. opt - optional software
    9. boot - boot loader files

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

## RHEL
1. Red Hat Enterprise Linux is a commercial linux distribution developed by Red Hat Inc (now IBM)
2. Commercial product with paid support, certification and long-term maintenance
3. Differences with Ubuntu
    1. RHEL focuses on enterprises, Ubuntu focuses on open source
    2. Uses RPM package format, Ubuntu uses DEB package format
    3. yum/dnf package management, apt
    4. XFS file system, ext4 file system

## RabbitMQ
1. RabbitMQ is an open-source message-broker/gateway which is easy to deploy on cloud environments or local machine

## Celery Python
1. Celeray Python is a popular, open-source python based task scheduler used for asynchronous execution outside of HTTP request-response cycle.
    1. Asynchronous Task Execution
    2. Distributed Task Execution
    3. Scheduling
    4. Concurrency
    5. Result Backends
    6. Integration with Frameworks

## FlaskAPI v/s FastAPI
| Feature                  | FlaskAPI                    | FastAPI                        |
| ------------------------ | --------------------------- | ------------------------------ |
| Performance              | Moderate (WSGI)             | High (ASGI, async-native)      |
| Learning Curve           | Low                         | Medium (typing + pydantic)     |
| Codebase Maturity        | Mature, stable              | Rapidly evolving, modern       |
| Documentation Generation | Manual or 3rd-party         | Automatic via OpenAPI          |
| Type Safety              | Optional                    | Strong, built-in with Pydantic |
| Use Case Fit             | Small tools, legacy systems | Scalable APIs, modern services |
