from django.urls import include, path
from rest_framework import routers
# from .views.CRUD import *
# from .views.prompting import *
from .views import prompting, CRUD

router = routers.DefaultRouter()

router.register(r'user', CRUD.UserViewSet)
router.register(r'species', CRUD.SpeciesViewSet)
router.register(r'animal', CRUD.AnimalViewSet)
router.register(r'transaction', CRUD.TransactionViewSet)
router.register(r'inventory', prompting.GetUserAnimals, basename='inventory')
router.register(r'created_by', prompting.GetCreatedBy, basename='created_by')
router.register(r'animal_history', prompting.GetAnimalHistory, basename='animal_history')
router.register(r'score', prompting.GetScore, basename='score')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
