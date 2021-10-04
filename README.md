# Task-4-Four
## Installation on GNU-Linux/MacOS
**The installation steps will be outlined here:**
- First step you need create virtual environment. More about [venv](https://docs.python.org/3/library/venv.html)  
**Creating venv on Linux/MacOS**
```
python3 -m venv venv
```
- Second step we need to activate **venv**:
```
source venv/bin/activate
```
## Database Setup
- Third step you need setup database
```
python manage.py makemigrations
python manage.py migrate
```
