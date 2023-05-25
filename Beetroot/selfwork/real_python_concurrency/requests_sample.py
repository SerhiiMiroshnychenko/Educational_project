import requests
import time

start_time = time.time()

for number in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print(f"--- {time.time() - start_time} seconds ---")