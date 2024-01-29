from django import forms
from marketplace.models import *
    
class ItemForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ('skin_name','weapon_type','description','price','image')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            self.add_error('price', 'Item price cannot be 0 or negative')
        return price
