from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

class User(models.Model):
    name = models.CharField(max_length=30, null=False, default=None, unique=True)
    password = EncryptedCharField(max_length=100, null=False, default=None)
    money = models.IntegerField(null=False, default=0)
    points = models.IntegerField(null=False, default=0)
    is_admin = models.BooleanField(null=False, default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Species(models.Model):
    name = models.CharField(max_length=40, null=False, unique=True, default=None)
    parent1 = models.ForeignKey("self", related_name="species_parent1", on_delete=models.DO_NOTHING, null=True)
    parent2 = models.ForeignKey("self", related_name="species_parent2", on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    creation_date = models.DateTimeField(auto_now_add=True)

class Animal(models.Model):
    name = models.CharField(max_length=30, null=False, default=None)
    owner = models.ForeignKey(User, related_name="owner", default=1, on_delete=models.SET_DEFAULT)
    species = models.ForeignKey(Species, max_length=30, null=False, default=None, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(User, related_name="creator", null=False, default=1, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(verbose_name="creation_date", auto_now_add=True)

class Transaction(models.Model):
    animal = models.ForeignKey(Animal, null=False, default=None, on_delete=models.DO_NOTHING)
    price = models.CharField(max_length=30, null=False, default=None)
    seller = models.ForeignKey(User, related_name="seller", null=False, default=1, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(User, related_name="buyer", null=True, default=1, on_delete=models.DO_NOTHING)
    date_sell_start = models.DateTimeField(auto_now_add=True)
    date_buy = models.DateTimeField(null=True)