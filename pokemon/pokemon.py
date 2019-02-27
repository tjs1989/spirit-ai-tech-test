try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

import requests
import json

r = requests.get('https://pokeapi.co/api/v2/ability/51/')

resultContent = json.loads(r.content)

resultContent = resultContent['pokemon']

lastResult = resultContent[len(resultContent) -1]

pokemonName = lastResult['pokemon']['name']

for pokemonSearch in search(pokemonName, tld="co.uk",start=0,stop=10):
    print(pokemonSearch)