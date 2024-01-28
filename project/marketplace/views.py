from django.shortcuts import render, redirect
from django.http import HttpResponse
from marketplace.models import *
from marketplace.forms import ItemForm

def market_view(request):
    weapons = Weapon.objects.all().order_by('skin_name')
    search_filter = request.GET.get('Search')

    if search_filter:
        weapons = Weapon.objects.filter(skin_name__icontains=search_filter)

    return render(
        request,
        'market_index.html',
        {'weapons': weapons},
        )

def new_item(request):
    if request.method == 'POST':
        new_item_form = ItemForm(request.POST)
        if new_item_form.is_valid():
            new_item_form.save()
            return redirect('market_index.html')
    else:
        new_item_form = ItemForm()

    return render(
        request,
        'new_item.html',{'new_item_form':new_item_form}
    )