from rest_framework import serializers

from .models import User, Species, Animal, Transaction

class UserSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    creator = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    species = serializers.CharField(read_only=True)
    parent1 = serializers.CharField(read_only=True)
    parent1_name = serializers.CharField(source='parent1.name', read_only=True)
    creator_name = serializers.CharField(source='creator.name', read_only=True)
    class Meta:
        model = Species
        fields = ('id', 'name', 'creation_date', 'parent1', 'parent2', 'creator', 'parent1_name', 'creator_name', 'species')

class AnimalSerializer(serializers.ModelSerializer):
    species_name = serializers.CharField(source='species.name', read_only=True)
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    creator_name = serializers.CharField(source='creator.name', read_only=True)
    class Meta:
        model = Animal
        fields = ('id', 'name', 'creation_date', 'creator', 'owner', 'species', 'species_name', 'owner_name', 'creator_name')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'