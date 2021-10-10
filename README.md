# Task-4-Four
## Installation on GNU-Linux/MacOS
**The installation steps will be outlined here:**
- First step you need create virtual environment. More read about [venv](https://docs.python.org/3/library/venv.html)  
**Creating venv on Linux/MacOS**
```
python3 -m venv venv
```
- Second step we need to activate **venv**:
```
source venv/bin/activate
```
## Install requirements
- Third step you need install requirements
```
pip install -r requirements.txt
```
## Database Setup
- Fourth step you need setup database
```
python manage.py makemigrations
python manage.py migrate
```
## Run Django Project locally  
- Fifth you can run django project from terminal
```
python manage.py runserver
```
## API docs
**API docs[/https://app.apiary.io/coursesapi7/editor]**
