# learning-python-django
tutorial to learn and create a sample django app


https://www.lynda.com/MyPlaylist/Watch/12698476/435068?autoplay=true

within Django, an app is more like a component, like a wiki, a blog or a wiki. A project is more like a site that uses all these apps. 

Files in an app:
models.py -- data layer
admin.py -- administrative interface
views.py -- control layer
tests.py -- tests
migrations/ -- holds migration files, which populates the db (?)

## SETUP

virtualenv my_env

my_env\Scripts\activate

now install Django into your venv with pip
pip install Django==1.8.6

verify:
python
    import django 
    django.VERSION


## STARTER PROJECT FILES:
django-admin startproject mysite

inside mysite, 
* manage.py has a bunch of commands you can run. execute the file to see a list. for example runserver
* __init__ tells django to treat the folder as a module
* wsgi, manage and init, do not edit

DO edit:
* settings.py configures django
* urls.py routes requests based on url

This is going to use SQLite as a DB, which is built in and good for development, not for production. 

### To add an app to this project

go to dir where manage.py is and startapp firstapp

now add this app to the settings file of the PROJECT (firstdjango)

## SETTINGS

lots more info here:

https://docs.djangoproject.com/en/1.11/topics/settings/

## Creating Models

in addition to the ones we used, 
there's also DecimalField, EmailFiend, URLField, FileField, ImageField, BooleanField, DateTimeField

field attributes get passed in as args:
* null=true means it's okay for there to be no data
* blank=true means it's okay for there to be an empty string as value for a text type field
* default sets a default value
* choices limits the values to an array

see django docs for more info https://docs.djangoproject.com/en/1.11/topics/db/models/