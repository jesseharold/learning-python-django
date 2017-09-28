# learning-python-django
tutorial to learn and create a sample django app


https://www.lynda.com/MyPlaylist/Watch/12698476/435068?autoplay=true

within Django, an app is more like a component, like a wiki, a blog or a wiki. A project is more like a site that uses all these apps. 

Files in an app:
models.py -- data layer
admin.py -- administrative interface
views.py -- control layer
tests.py -- tests
migrations/ -- holds migration files, which change the db structure over time as data is added 

## SETUP

````virtualenv my_env````

my_env\Scripts\activate````

now install Django into your venv with pip
````pip install Django==1.8.6````

verify:
python
    import django 
    django.VERSION


## STARTER PROJECT FILES:
````django-admin startproject mysite````

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

https://docs.djangoproject.com/en/1.11/topics/db/models/#field-types

just writing a model doesn't create a db table, though. You need an initial migration for that!

## Migrations

Migrations are needed any time models are added, fields are added or removed or the attributes are changed.

````python manage.py makemigrations````
generates migration files, based on differences between the models files and the current db

````python manage.py migrate````
runs all migrations that haven't been run yet (called unapplied migrations)
use --list option to show them

use DB Browser for SQLite to inspect your db. table is named [appname]_[modelname]

## register models

updated admin.py to register the new model with the app. 

then create superuser using manage.py

````python manage.py createsuperuser````

for local use only, non-secure pw is jesse/password

you can use this to log in to the admin interface of your app, which is at localhost:8000/admin

## ADMIN INTERFACE

inside your model, you can add an item, the UI has the fields you set up! neat!

customize the display of items in the admin interface by adding a class to admin.py that inherits from admin.ModelAdmin

## WORKING WITH DATA

````python manage.py shell```

opens up a python interface