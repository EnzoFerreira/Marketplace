from django.db import models

class Weapon_type(models.Model):
    id = models.AutoField(primary_key=True)
    weapon_type = models.CharField(max_length=100)

    def __str__(self):
        return self.weapon_type

class Weapon(models.Model):
    id = models.AutoField(primary_key=True)
    skin_name = models.CharField(max_length=50)
    weapon_type = models.ForeignKey(Weapon_type, null=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='marketplace/', null=True)

    def __str__(self):
        return self.skin_name
