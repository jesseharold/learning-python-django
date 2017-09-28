from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

# these views are definted in urls.py

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
        'items': items,
    })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404("This item does not exist")
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })

# the curly braces followed by .format is called string interpolation, and it puts the value of id into the braces slot. you can have more than one value, which is why it's a number, 0 is the first value