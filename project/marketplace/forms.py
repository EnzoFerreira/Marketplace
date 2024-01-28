from django import forms
from marketplace.models import *
    
class ItemForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ('skin_name','weapon_type','description','price','image')