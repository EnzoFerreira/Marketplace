from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from marketplace.models import *
from marketplace.forms import ItemForm
from django.views import View
from django.views.generic import ListView,CreateView,DetailView

class WeaponsListView(ListView):
    model = Weapon
    template_name = 'market_index.html'
    context_object_name = 'weapons'

    def get_queryset(self):
        weapons = super().get_queryset().order_by('skin_name')
        search = self.request.GET.get('Search')
        if search:
            weapons = weapons.filter(skin_name__icontains=search)
        return weapons
class new_market_item(CreateView):
    model = Weapon
    form_class = ItemForm
    template_name = 'new_item.html'
    success_url = '/csmarket/'

class Weapon_View(DetailView):
    model = Weapon
    template_name = 'weapon_view.html'
