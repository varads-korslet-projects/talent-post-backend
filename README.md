# Talent Post backend
## Setting up a development environment
Creating a virtual environment: 
```python -m venv venv```

Find specific instructions to activate the environment at:
https://docs.python.org/3/tutorial/venv.html

Install reuirements: ```pip install -r requirements.txt```

## Starting the development server:
Create required directories
```
cd TalentPost
mkdir media
mkdir media/Audio
mkdir media/Files
mkdir media/Images
mkdir media/Video
mkdir static
mkdir static/assets
mkdir statis/css
mkdit static/js
```

Create the database
```
python manage.py makemigrations
python manage.py migrate
```

Running the server
```
python manage.py runserver
```