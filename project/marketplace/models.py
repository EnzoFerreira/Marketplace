from django.db import models

class Weapon_type(models.Model):
    id = models.AutoField(primary_key=True)
    weapon_type = models.CharField(max_length=100)

    def __str__(self):
        return self.weapon_type

class Weapon(models.Model):
    id = models.AutoField(primary_key=True)
    weapon_name = models.CharField(null = True, max_length=50)
    skin_type = models.CharField(null= True, max_length=150)
    weapon_type = models.ForeignKey(Weapon_type, null=True, on_delete=models.PROTECT)
    exterior = models.CharField(max_length=100, blank=True)
    float = models.FloatField(null=True)
    description = models.CharField(null = True,blank=True, max_length=200)
    price = models.FloatField(null = True)
    image = models.ImageField(null = True, upload_to='marketplace/')

    def __str__(self):
        return self.weapon_name

class Weapon_inventory(models.Model):
    weapon_count = models.IntegerField()
    weapon_value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.weapon_count} | {self.weapon_value}'