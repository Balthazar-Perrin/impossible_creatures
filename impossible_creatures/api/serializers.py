from rest_framework import serializers

from .models import User, Species, Animal, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    parent1 = serializers.CharField(source='parent1.name', read_only=True)
    parent2 = serializers.CharField(source='parent2.name', read_only=True)
    creator = serializers.CharField(source='creator.name', read_only=True)

    class Meta:
        model = Species
        fields = ('id', 'name', 'creation_date', 'parent1_id', 'parent2_id', 'creator_id', 'parent1', 'parent2', 'creator')

class AnimalSerializer(serializers.ModelSerializer):
    species = serializers.CharField(source='species.name', read_only=True)
    owner = serializers.CharField(source='owner.name', read_only=True)
    creator = serializers.CharField(source='creator.name', read_only=True)
    class Meta:
        model = Animal
        fields = ('id', 'name', 'creation_date', 'creator_id', 'owner_id', 'species_id', 'species', 'owner', 'creator')

class TransactionSerializer(serializers.ModelSerializer):
    buyer = serializers.CharField(source='buyer.name', read_only=True)
    seller = serializers.CharField(source='seller.name', read_only=True)
    animal = serializers.CharField(source='animal.name', read_only=True)
    class Meta:
        model = Transaction
        fields = ('id', 'price', 'date_sell_start', 'date_buy', 'animal_id', 'buyer_id', 'seller_id', 'buyer', 'seller', 'animal')