from ..serializers import UserSerializer, SpeciesSerializer, AnimalSerializer, TransactionSerializer
from ..models import User, Species, Animal, Transaction
import json

from rest_framework import viewsets
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from django.http import HttpResponse

class GetUserAnimals(viewsets.ViewSet):

    def retrieve(self, request, pk):
        queryset = Animal.objects.filter(owner_id=pk)
        print(queryset)
        result = get_list_or_404(queryset)
        objects = []
        for animal in result:
            serializer = AnimalSerializer(animal)
            objects.append(serializer.data)
        return HttpResponse(json.dumps(objects), content_type="text/json")


class GetCreatedBy(viewsets.ViewSet):
    def retrieve(self, request, pk):
        queryset = Animal.objects.filter(creator_id=pk)
        result = get_list_or_404(queryset)
        objects = []
        for animal in result:
            serializer = AnimalSerializer(animal)
            objects.append(serializer.data)
        
        return HttpResponse(json.dumps(objects), content_type="text/json")

class GetAnimalHistory(viewsets.ViewSet):
    def retrieve(self, request, pk):
        q0 = Animal.objects.get(id=pk)
        current_owner = AnimalSerializer(q0).data.get('owner')

        history = [current_owner]

        q1 = Transaction.objects.filter(animal_id=pk).order_by('date_buy').exclude(buyer__isnull=True)
        # print(q1)
        transactions = get_list_or_404(q1)
        # print(transactions)
        for trans in transactions:
            serializer = TransactionSerializer(trans)
            history.append(serializer.data.get('seller'))
        return HttpResponse(json.dumps(history), content_type="text/json")


class GetScore(viewsets.ViewSet):
    def retrieve(self, request, pk):
        index = int(pk)
        queryset = User.objects.all().order_by('-points')[:index]
        print(queryset)
        if index == 1 :
            return HttpResponse(json.dumps(UserSerializer(queryset).data), content_type="text/json")
        
        result=get_list_or_404(queryset)

        objects = []
        for user in result:
            serializer = UserSerializer(user)
            objects.append(serializer.data)
        
        return HttpResponse(json.dumps(objects), content_type="text/json")