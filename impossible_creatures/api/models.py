from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager

class MyMgr(BaseUserManager):
    def create_user(self, username='', password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        user = self.model(
            username=username,
        )

        user.save(using=self._db)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, null=False, default=None, unique=True)
    money = models.IntegerField(null=False, default=0)
    points = models.IntegerField(null=False, default=0)
    is_admin = models.BooleanField(null=False, default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    objects = MyMgr()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Species(models.Model):
    name = models.CharField(max_length=40, null=False, unique=True, default=None)
    parent1_id = models.ForeignKey("self", related_name="species_parent1", on_delete=models.DO_NOTHING, null=True)
    parent2_id = models.ForeignKey("self", related_name="species_parent2", on_delete=models.DO_NOTHING, null=True)
    creator_id = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    creation_date = models.DateTimeField(auto_now_add=True)

class Animal(models.Model):
    name = models.CharField(max_length=30, null=False, default=None)
    owner_id = models.ForeignKey(User, related_name="owner", default=1, on_delete=models.SET_DEFAULT)
    species_id = models.ForeignKey(Species, max_length=30, null=False, default=None, on_delete=models.DO_NOTHING)
    creator_id = models.ForeignKey(User, related_name="creator", null=False, default=1, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(verbose_name="creation_date", auto_now_add=True)

class Transaction(models.Model):
    animal_id = models.ForeignKey(Animal, null=False, default=None, on_delete=models.DO_NOTHING)
    price = models.CharField(max_length=30, null=False, default=None)
    seller_id = models.ForeignKey(User, related_name="seller", null=False, default=1, on_delete=models.DO_NOTHING)
    buyer_id = models.ForeignKey(User, related_name="buyer", null=True, default=1, on_delete=models.DO_NOTHING)
    date_sell_start = models.DateTimeField(auto_now_add=True)
    date_buy = models.DateTimeField(null=True)