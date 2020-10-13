from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Species, Animal, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    parent1= serializers.CharField(source='parent1_id.name', read_only=True)
    parent2 = serializers.CharField(source='parent2_id.name', read_only=True)
    creator = serializers.CharField(source='creator_id.username', read_only=True)

    class Meta:
        model = Species
        fields = ('id', 'name', 'creation_date', 'parent1_id', 'parent2_id', 'creator_id', 'parent1', 'parent2', 'creator')

class AnimalSerializer(serializers.ModelSerializer):
    species = serializers.CharField(source='species_id.name', read_only=True)
    owner = serializers.CharField(source='owner_id.username', read_only=True)
    creator = serializers.CharField(source='creator_id.username', read_only=True)
    class Meta:
        model = Animal
        fields = ('id', 'name', 'creation_date', 'creator_id', 'owner_id', 'species_id', 'species', 'owner', 'creator')

class TransactionSerializer(serializers.ModelSerializer):
    buyer = serializers.CharField(source='buyer_id.username', read_only=True)
    seller = serializers.CharField(source='seller_id.username', read_only=True)
    animal = serializers.CharField(source='animal_id.username', read_only=True)
    class Meta:
        model = Transaction
        fields = ('id', 'price', 'date_sell_start', 'date_buy', 'animal_id', 'buyer_id', 'seller_id', 'buyer', 'seller', 'animal')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")
