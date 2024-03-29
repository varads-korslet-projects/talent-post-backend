# Talent Post backend
## Setting up a development environment
Creating a virtual environment: 
```python -m venv venv```

Find specific instructions to activate the environment at:
https://docs.python.org/3/tutorial/venv.html

Install reuirements: ```pip install -r requirements.txt```

## Starting the development server:
Create the database
```
cd TalentPost
python manage.py makemigrations
python manage.py migrate
```
Running the server
```
python manage.py runserver
```