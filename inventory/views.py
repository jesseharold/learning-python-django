from django.shortcuts import render
from django.http import HttpResponse

# these views are definted in urls.py

def index(request):
    return HttpResponse('<p>In index view</p>')

def item_detail(request, id):
    return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))

# the curly braces followed by .format is called string interpolation, and it puts the value of id into the braces slot. you can have more than one value, which is why it's a number, 0 is the first value