from django.urls import path, include
from rest_framework import routers

from pokemon.api.viewsets import PokemonViewSet

app_name = 'pokemon'

router = routers.DefaultRouter(trailing_slash=False)
router.register('pokemons/?', PokemonViewSet, basename='Pokemons')

urlpatterns = [
    path('api/', include(router.urls)),
]
