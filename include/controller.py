import requests
from .db import SessionLocal, engine, Base
from .models import Pokemon
from .schema import PokemonSchema
from random import randint
Base.metadata.create_all(bind=engine)

def gerar_numero_aleatorio():
    return randint(1, 350)

def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    print(response)
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchema(name=data['name'], type=types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        existing_pokemon = db.query(Pokemon).filter(Pokemon.name == pokemon_schema.name).first()
        if existing_pokemon:
            print(f"Pokémon {pokemon_schema.name} já existe no banco de dados.")
            return {"name": existing_pokemon.name, "type": existing_pokemon.type}
        
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
        return {"name": db_pokemon.name, "type": db_pokemon.type}  # JSON serializável

