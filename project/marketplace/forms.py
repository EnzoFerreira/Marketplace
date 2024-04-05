from django import forms
from marketplace.models import *
    
class ItemForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ('weapon_name','skin_type','weapon_type','exterior','float','description','price','image')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            self.add_error('price', 'Item price cannot be 0 or negative')
        return price
    def clean_exterior(self):
        exterior = self.cleaned_data.get('exterior')
        if exterior == '':
            self.add_error('exterior', 'Please enter the exterior of the item')
        return exterior
    def clean_float(self):
        float = self.cleaned_data.get('float')
        if float == None:
            self.add_error('price', 'Item float cannot be null')
        return float
