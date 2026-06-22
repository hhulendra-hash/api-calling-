import requests

def get_pokemon_data(pokemon_name):
    # Convert name to lowercase to match PokéAPI requirements
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract basic details
            name = data['name'].capitalize()
            poke_id = data['id']
            types = [t['type']['name'] for t in data['types']]
            sprite_url = data['sprites']['front_default']
            
            # Extract specific stats
            stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
            
            print(f"--- Pokémon ID #{poke_id}: {name} ---")
            print(f"Types: {', '.join(types)}")
            print(f"Base HP: {stats.get('hp')}")
            print(f"Base Attack: {stats.get('attack')}")
            print(f"Sprite Image URL: {sprite_url}")
            
        elif response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found. Check your spelling.")
        else:
            print(f"Failed to fetch data. HTTP Status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

# Test the function
get_pokemon_data("ditto")