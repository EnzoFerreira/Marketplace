from django.contrib import admin
from marketplace.models import *
class weaponAdmin(admin.ModelAdmin):
    list_display = ('skin_name','weapon_type')
    search_fields = ('skin_name','weapon_type')

class weapontypeAdmin(admin.ModelAdmin):
    list_display = ('weapon_type',)
    search_fields = ('weapon_type',)

admin.site.register(Weapon_type, weapontypeAdmin)
admin.site.register(Weapon, weaponAdmin)
