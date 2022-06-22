import django, os, requests
from tqdm import tqdm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from pokemon.models import Pokemon

def populate():
    pokemons_list = []
    for i in tqdm(range(151)):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{ i+1 }')
        response = response.json()
        pokemon_types = [t['type']['name'].title() for t in response['types']]
        pokemon_data = {
            'number': response['id'],
            'name': response['name'].title(),
            'types': ' '.join(pokemon_types),
            'height': response['height'],
            'weight': response['weight'],
            'sprite': response['sprites']['other']['dream_world']['front_default'],
        }
        pokemon = Pokemon(**pokemon_data)
        pokemons_list.append(pokemon)
    Pokemon.objects.bulk_create(pokemons_list)
    print('Pokemons created successfully!')

populate()
