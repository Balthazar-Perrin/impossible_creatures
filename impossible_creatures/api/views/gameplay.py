from rest_framework import viewsets
from ..serializers import UserSerializer, SpeciesSerializer, AnimalSerializer, TransactionSerializer
from ..models import User, Species, Animal, Transaction

from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from rest_framework import status
from rest_framework.response import Response

class Fusion(viewsets.ViewSet):
	def create(self, request, *args, **kwargs):
		print(request.data)
		animalPar1 = Animal.objects.get(id=request.data['animal1_id'])
		speciesParent1 = Species.objects.get(id=AnimalSerializer(animalPar1).data.get('species_id'))

		animalPar2 = Animal.objects.get(id=request.data['animal2_id'])
		speciesParent2 = Species.objects.get(id=AnimalSerializer(animalPar2).data.get('species_id'))

		owner = User.objects.get(id="10")
		try:
			newSpecies = Species.objects.get(parent1_id=AnimalSerializer(animalPar1).data.get('species_id'), parent2_id=AnimalSerializer(animalPar2).data.get('species_id'))
			
			newDict = {}
			newDict['name'] = request.data['nameAnimal']
			newDict['species_id'] = SpeciesSerializer(newSpecies).data.get('id')
			animalSerializer = AnimalSerializer(data=newDict)
			if animalSerializer.is_valid():
				animalSerializer.save()
			newDict = {}
			newDict['money'] = UserSerializer(owner).data.get('money') + 250
			userSerializer = UserSerializer(owner, data=newDict)
			if userSerializer.is_valid():
				userSerializer.save()
			deletePar1 = animalPar1.delete()
			deletePar2 = animalPar2.delete()
			return Response("A new animal has been created.", status=status.HTTP_201_CREATED)

		except ObjectDoesNotExist :
			
			speciesSerializer = SpeciesSerializer(data=request.data)
			if speciesSerializer.is_valid():
				speciesSerializer.save(name=request.data['name'], parent1_id=speciesParent1, parent2_id=speciesParent2)
				newDict = {}
				newDict['name'] = request.data['nameAnimal']
				newDict['species_id'] = speciesSerializer.data['id']
				animalSerializer = AnimalSerializer(data=newDict)
				if animalSerializer.is_valid():
					animalSerializer.save()
				newDict = {}
				newDict['money'] = UserSerializer(owner).data.get('money') + 500
				userSerializer = UserSerializer(owner, data=newDict)
				if userSerializer.is_valid():
					userSerializer.save()
				deletePar1 = animalPar1.delete()
				deletePar2 = animalPar2.delete()
				return Response("You discovered a new Species!", status=status.HTTP_201_CREATED)
		return Response("Error.", status=status.HTTP_400_BAD_REQUEST)

def up(q0, ser, parents):
        parent1=ser(q0).data.get('parent1_id')
        parent2=ser(q0).data.get('parent2_id')

        if parent1 is not None:
            q1=Species.objects.get(id=parent1)
            if (ser(q1).data.get('parent1_id') == None and ser(q1).data.get('parent2_id') == None):
                parents.append("[base]"+ser(q1).data.get('name'))
            else:
                parents.append(ser(q1).data.get('name'))
            up(q1, ser, parents)

        if parent2 is not None:
            q2=Species.objects.get(id=parent2)
            if (ser(q2).data.get('parent1_id') == None and ser(q2).data.get('parent2_id') == None):
                parents.append("[base]"+ser(q2).data.get('name'))
            else:
                parents.append(ser(q2).data.get('name'))
            up(q2, ser, parents)

        return parents

class GetParents(viewsets.ViewSet):

    def retrieve(self, request, pk):
        ser = SpeciesSerializer
        q0=Animal.objects.get(id=pk)
        speciesId = AnimalSerializer(q0).data.get('species_id')
        q0=Species.objects.get(id=speciesId)

        parents = []    
        return HttpResponse(json.dumps(up(q0, ser, parents)))

class GetPercents(viewsets.ViewSet):

    def retrieve(self, request, pk):
        ser = SpeciesSerializer
        q0=Species.objects.get(id=pk)
        temp = [] 
        baseparents = []  
        parents = up(q0, ser, temp)
        for parent in parents:
            if parent.startswith('[base]'):
                baseparents.append(parent[6:])
        percents = dict((i, str(baseparents.count(i)*100/len(baseparents))+"%") for i in baseparents)

        return HttpResponse(json.dumps(percents))
		
class Sell(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        print(request)
        try :
            print('oui')
            animal = Animal.objects.get(id=request.data['animal_id'], owner_id=request.data['user_id'])
            print('anmal')

            newDict = {}
            newDict['price'] = request.data['price']
            newDict['animal_id'] = request.data['animal_id']
            newDict['seller_id'] = request.data['user_id']
            ser = TransactionSerializer(data=newDict)
            if ser.is_valid():
                    ser.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response("You do not own this animal", status=status.HTTP_400_BAD_REQUEST)