from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, filters, viewsets
from rest_framework.response import Response
from pokemon.models import Pokemon
from .serializers import PokemonSerializer

class Pagination20(pagination.PageNumberPagination):
    '''Número de elementos listados por página'''
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })


class PokemonViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Pokemons to be viewed or edited.'''
    http_method_names = ['get']
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['number']
    search_fields = ['name', 'types']
    pagination_class = Pagination20

    @method_decorator(cache_page(300))
    def dispatch(self, *args, **kwargs):
        return super(PokemonViewSet, self).dispatch(*args, **kwargs)
