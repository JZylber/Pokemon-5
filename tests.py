from classes import WaterType, FireType, PlantType
from battle import pokemon_battle

class TestPokemon:
    def test_init_water(self):
        pokemon = WaterType('Squirtle',0)
        assert pokemon.name == 'Squirtle'
        assert pokemon.lvl == 0
        assert pokemon.hp == 42
        assert pokemon.atk == 5.1
        assert pokemon.type == 'Water'

    def test_init_fire(self):
        pokemon = FireType('Charmander',0)
        assert pokemon.name == 'Charmander'
        assert pokemon.lvl == 0
        assert pokemon.hp == 40
        assert pokemon.atk == 5.3
        assert pokemon.type == 'Fire'
    
    def test_init_plant(self):
        pokemon = PlantType('Bulbasaur',0)
        assert pokemon.name == 'Bulbasaur'
        assert pokemon.lvl == 0
        assert pokemon.hp == 45
        assert pokemon.atk == 4.9
        assert pokemon.type == 'Plant'
    
    def test_lvl_up_water(self):
        pokemon = WaterType('Squirtle',10)
        assert pokemon.lvl == 10
        assert pokemon.hp == 84
        assert pokemon.atk == 10.2

    def test_lvl_up_fire(self):
        pokemon = FireType('Charmander',10)
        assert pokemon.lvl == 10
        assert pokemon.hp == 80
        assert pokemon.atk == 10.6

    def test_lvl_up_plant(self):
        pokemon = PlantType('Bulbasaur',10)
        assert pokemon.lvl == 10
        assert pokemon.hp == 90
        assert pokemon.atk == 9.8

class TestAttack:
    def test_take_damage_integer(self):
        pokemon = WaterType('Squirtle',10)
        pokemon.take_damage(10)
        assert pokemon.hp == 74

    def test_take_damage_float_truncate(self):
        pokemon = WaterType('Squirtle',10)
        pokemon.take_damage(10.4)
        assert pokemon.hp == 74

    def test_take_damage_float_round(self):
        pokemon = WaterType('Squirtle',10)
        pokemon.take_damage(10.6)
        assert pokemon.hp == 73

    def test_fainted(self):
        pokemon = WaterType('Squirtle',10)
        assert not pokemon.fainted()
        pokemon.take_damage(100)
        assert pokemon.fainted()


    def test_attack_water_fire(self):
        pokemon1 = WaterType('Squirtle',10)
        pokemon2 = FireType('Charmander',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 60

    def test_attack_fire_water(self):
        pokemon1 = FireType('Charmander',10)
        pokemon2 = WaterType('Squirtle',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 79

    def test_attack_water_plant(self):
        pokemon1 = WaterType('Squirtle',10)
        pokemon2 = PlantType('Bulbasaur',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 85

    def test_attack_plant_water(self):
        pokemon1 = PlantType('Bulbasaur',10)
        pokemon2 = WaterType('Squirtle',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 64

    def test_attack_fire_plant(self):
        pokemon1 = FireType('Charmander',10)
        pokemon2 = PlantType('Bulbasaur',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 69

    def test_attack_plant_fire(self):
        pokemon1 = PlantType('Bulbasaur',10)
        pokemon2 = FireType('Charmander',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 75

    def test_attack_fire_fire(self):
        pokemon1 = FireType('Charmander',10)
        pokemon2 = FireType('Charmander',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 69

    def test_attack_water_water(self):
        pokemon1 = WaterType('Squirtle',10)
        pokemon2 = WaterType('Squirtle',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 74

    def test_attack_plant_plant(self):
        pokemon1 = PlantType('Bulbasaur',10)
        pokemon2 = PlantType('Bulbasaur',10)
        damage = pokemon1.attack(pokemon2)
        assert pokemon2.hp == 80

class TestBattle:
    def test_battle_pokemon_2_wins_first_turn(self):
        pokemon1 = PlantType('Bulbasaur',0)
        pokemon2 = FireType('Charmander',40)
        winner = pokemon_battle(pokemon1, pokemon2)
        assert winner == pokemon2
        assert pokemon1.fainted()
        assert not pokemon2.fainted()
        assert pokemon2.hp == 198
    def test_battle_pokemon_1_wins_first_turn(self):
        pokemon1 = FireType('Charmander',40)
        pokemon2 = PlantType('Bulbasaur',0)
        winner = pokemon_battle(pokemon1, pokemon2)
        assert winner == pokemon1
        assert not pokemon1.fainted()
        assert pokemon2.fainted()
        assert pokemon1.hp == 200
    def test_battle_pokemon_2_wins_many_turns(self):
        pokemon1 = FireType('Charmander',10)
        pokemon2 = WaterType('Squirtle',10)
        winner = pokemon_battle(pokemon1, pokemon2)
        assert winner == pokemon2
        assert pokemon1.fainted()
        assert not pokemon2.fainted()
        assert pokemon2.hp == 64
    def test_battle_pokemon_1_wins_many_turns(self):
        pokemon1 = PlantType('Bulbasaur',10)
        pokemon2 = WaterType('Squirtle',10)
        winner = pokemon_battle(pokemon1, pokemon2)
        assert winner == pokemon1
        assert not pokemon1.fainted()
        assert pokemon2.fainted()
        assert pokemon1.hp == 70



    
    