from django.db.models.signals import *
from django.dispatch import receiver
from marketplace.models import *
from django.db.models import Sum

def weapon_update_inventory():
    weapon_count = Weapon.objects.all().count()
    weapon_value = Weapon.objects.aggregate(
        total_value=Sum('price')
    )['total_value']

    Weapon_inventory.objects.get_or_create(
        weapon_count = weapon_count,
        weapon_value = weapon_value
    )

@receiver(pre_save, sender = Weapon)
def weapon_pre_save(sender, instance, **kwargs): 
    if not instance.description:
        #TODO
        #FInd a way to reference the model name[]
        #URL request to weapon description[]
        instance.description = 'TBC'


@receiver(post_save, sender = Weapon)
def weapon_post_save(sender, instance, **kwargs):
    weapon_update_inventory()

@receiver(pre_delete, sender = Weapon)
def weapon_pre_delete(sender, instance, **kwargs):
    pass

@receiver(post_delete, sender = Weapon)
def weapon_post_delete(sender, instance, **kwargs):
    weapon_update_inventory()