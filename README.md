# Goodreads Competition Enterer

## Installation Guide

Install `pyenv` 
```bash
pyenv install 3.13.1
pyenv local 3.13.1
```

Activate the `goodreads` virtual env for the project
```bash
python -m venv goodreads_env
source goodreads_env/bin/activate
```

Install the requirements for the project
```bash
pip install -r requirements.txt
```


## Requirements

Creating a Django application that uses Python, Playwrite, and Celery to interact with Goodreads


## Running the application

localhost:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```