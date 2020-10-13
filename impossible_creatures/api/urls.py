from django.urls import include, path
from rest_framework import routers
from .views import CRUD, prompting, gameplay, authentification
from knox import views as knox_views

router = routers.DefaultRouter()

router.register(r'user', CRUD.UserViewSet)
router.register(r'species', CRUD.SpeciesViewSet)
router.register(r'animal', CRUD.AnimalViewSet, basename='animals')
router.register(r'transaction', CRUD.TransactionViewSet)
router.register(r'inventory', prompting.GetUserAnimals, basename='inventory')
router.register(r'created_by', prompting.GetCreatedBy, basename='created_by')
router.register(r'animal_history', prompting.GetAnimalHistory, basename='animal_history')
router.register(r'score', prompting.GetScore, basename='score')
router.register(r'fusion', gameplay.Fusion, basename='fusion')
router.register(r'login', CRUD.Login, basename='login')
router.register(r'parents', gameplay.GetParents, basename='getparents')
router.register(r'percents', gameplay.GetPercents, basename='percents')

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('knox.urls')),
    path('auth/register', authentification.RegisterAPI.as_view()),
    path('auth/login', authentification.LoginAPI.as_view())
]
