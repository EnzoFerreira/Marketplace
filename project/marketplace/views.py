from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from marketplace.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from marketplace.forms import ItemForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import *

class WeaponsListView(ListView):
    model = Weapon
    template_name = 'market_index.html'
    context_object_name = 'weapons'

    def get_queryset(self):
        weapons = super().get_queryset().order_by('weapon_name')
        search = self.request.GET.get('Search')
        if search:
            if weapons.filter(weapon_name__icontains=search):
                weapons = weapons.filter(weapon_name__icontains=search)
            if weapons.filter(skin_type__icontains=search):
                weapons = weapons.filter(skin_type__icontains=search)
        return weapons
@method_decorator(login_required(login_url='login'), name='dispatch')
class new_market_item(CreateView):
    model = Weapon
    form_class = ItemForm
    template_name = 'new_item.html'
    success_url = '/csmarket/'

class Weapon_View(DetailView):
    model = Weapon
    template_name = 'weapon_view.html'

class Weapon_edit(UpdateView):
    model = Weapon
    form_class = ItemForm
    template_name = 'weapon_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('weapon_details', kwargs={'pk': self.object.pk})

class Weapon_delete(DeleteView):
    model = Weapon
    template_name = 'weapon_delete.html'
    success_url = '/csmarket/'