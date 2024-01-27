from django.shortcuts import render
from django.http import HttpResponse
from marketplace.models import *

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
