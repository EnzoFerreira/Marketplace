import urllib.request
from django.db.models.signals import *
from django.dispatch import receiver
from marketplace.models import *
from django.db.models import Sum
from django.shortcuts import get_object_or_404
import requests
from bs4 import BeautifulSoup
from lxml import html

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
        #If´s for classes and specific weapons
        weapon_name = instance.weapon_name.replace(' ', '-')
        
        weapon_name_final = f'{weapon_name}'.upper()

        if 'KNIFE' in weapon_name_final:
            
            knife_name = weapon_name_final.capitalize()
            if 'knife' in knife_name:
                replace1 = knife_name.replace('k','K')
                replace2 = replace1.replace('-','_')

            url = f'https://liquipedia.net/counterstrike/{replace2}'
            request = requests.get(url)
            html_request = html.fromstring(request.content)

            description = []

            for i in html_request.xpath('//*[@id="mw-content-text"]/div/blockquote/div[1]'):
                response = i.text_content().strip()
                if response != '':
                    description.append(response)
                else: 
                    weapon_name = weapon_name_final.lower()
                    url = f'https://wiki.cs.money/weapons/{weapon_name}'
                    request = requests.get(url)
                    html_request = html.fromstring(request.content)
                    
                    for i in html_request.xpath('//*[@id="skins"]/div[1]/div/div[3]/div/div'):
                        response = i.text_content().strip()
                        if response:
                            description.append(response)
                instance.description = description[0]

        if 'GALIL' in weapon_name_final:
            url = f'https://liquipedia.net/counterstrike/Galil_AR'
            request = requests.get(url)
            html_request = html.fromstring(request.content)

            description = []

            for i in html_request.xpath('//*[@id="mw-content-text"]/div/blockquote/div[1]'):
                response = i.text_content().strip()
                if response:
                    description.append(response)
                instance.description = description[0]

        if 'SHADOW' in weapon_name_final:
            url = f'https://liquipedia.net/counterstrike/Shadow_Daggers'
            request = requests.get(url)
            html_request = html.fromstring(request.content)

            description = []

            for i in html_request.xpath('//*[@id="mw-content-text"]/div/blockquote/div[1]'):
                response = i.text_content().strip()
                if response:
                    description.append(response)
                instance.description = description[0]
        else:
            url = f'https://liquipedia.net/counterstrike/{weapon_name_final}'
            request = requests.get(url)
            html_request = html.fromstring(request.content)

            description = []

            for i in html_request.xpath('//*[@id="mw-content-text"]/div/blockquote/div[1]'):
                response = i.text_content().strip()
                if response != '':
                    description.append(response)
                instance.description = description[0]
            
            if description == []:
                weapon_name = weapon_name_final.lower()
                url = f'https://wiki.cs.money/weapons/{weapon_name}'
                request = requests.get(url)
                html_request = html.fromstring(request.content)
                
                for i in html_request.xpath('//*[@id="skins"]/div[1]/div/div[3]/div/div'):
                    response = i.text_content().strip()
                    if response:
                        description.append(response)
                    instance.description = description[0]




@receiver(post_save, sender = Weapon)
def weapon_post_save(sender, instance, **kwargs):
    weapon_update_inventory()

@receiver(pre_delete, sender = Weapon)
def weapon_pre_delete(sender, instance, **kwargs):
    pass

@receiver(post_delete, sender = Weapon)
def weapon_post_delete(sender, instance, **kwargs):
    weapon_update_inventory()