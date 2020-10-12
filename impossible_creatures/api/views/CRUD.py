from rest_framework import viewsets
from ..serializers import UserSerializer, SpeciesSerializer, AnimalSerializer, TransactionSerializer
from ..models import User, Species, Animal, Transaction

from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
class Login(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = User.objects.get(name=request.data['login'], password=request.data['password'])
            return HttpResponse(json.dumps(UserSerializer(queryset).data), status="200")

        except ObjectDoesNotExist :
            return HttpResponse("Your inputs didn't match any credentials in our database", status="400")
