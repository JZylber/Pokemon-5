# Pokémon

## Introducción

*La introducción fue escrita por ChatGPT y editada por mí*

Los Pokémon son criaturas ficticias que existen en el universo de los videojuegos, series de televisión y cartas coleccionables de Pokémon. Cada Pokémon tiene su propia apariencia, habilidades y estadísticas, como puntos de vida (HP), ataque y nivel. Además, cada Pokémon pertenece a uno o más tipos elementales, como Fuego, Agua, Planta, Eléctrico, entre otros. Estos tipos juegan un papel fundamental en las batallas Pokémon, ya que cada tipo tiene fortalezas y debilidades frente a otros.

## Tests

Esta vuelta los tests los escribí yo! No solo están separados en *TestSuites* (conjuntos de tests) sino que se autocorren al pushear el repositorio. Para verificar que toda la consigna esté bien hecha, pueden correr

```python -m pytest tests.py```

## Consigna

### Punto 1 - Pokémon

Completar las 3 clases Pokémon, `WaterType`, `FireType`, `PlantType` (en el archivo `classes.py`) que desciendan de una clase padre (abstracta). Las clases deben cumplir lo siguiente:
- Inicializarse con un nombre (`string`) y un nivel (`integer`), que deben guardarse en el atributo `name` y `lvl` respectivamente.
- Iniciar con un atributo `hp` que se inicialice con el siguiente valor `(base_hp_tipo)x(1 + nivel/10)`. El atributo base por tipo se encuentra en la tabla debajo.
- Iniciar con un atributo `atk` que se inicialice con el siguiente valor `(base_ataque_tipo)x(1 + nivel/10)`. El atributo base por tipo se encuentra en la tabla debajo.

Atributos base (o su valor en nivel 0):
|Tipo|HP|Ataque|
|---|---|---|
|`PlantType`|45|4.9|
|`FireType`|40|5.3|
|`WaterType`|42|5.1|

**Pueden agregar otras cosas que necesiten para que la clase funcione.** ¡Piensen que cosas van a la clase padre!

#### TESTS

Para verificar que este punto esté bien pueden correr

```python -m pytest tests.py::TestPokemon```

### Punto 2 - Ataques

Ahora vamos a hacer que puedan atacar. Para eso, en las 3 clases tienen que hacer lo siguiente:
- Crear el método `take_damage` que tome un daño(`int` o `float`), y se lo reste al hp. El hp debe permanecer un número entero, por lo tanto los números decimales los *redondea* antes de restar.
- Crear el método `fainted` que devuelva un `boolean`(`True` o `False`) si el pókemon está desmayado. Se considera desmayado si recibió tanto daño como su `hp` o más.
- Crear el método `attack` que tome a otro pokémon y le saque tanto daño como ataque tiene **multiplicado por un factor que depende de los tipos de ambos**. Este multiplicador se debe a que los tipos tienen fortalezas y debilidades frente a otros tipos, que aumentan o reducen su efectividad. Por ejemplo, los tipo fuego multiplican su daño x2 para los tipo planta y por la mitad para los tipo agua. Debajo se encuentra la tabla con los multiplicadores:

|Atacante\Defensor|`PlantType`|`FireType`|`WaterType`|
|---|---|---|---|
|`PlantType`|x1|x0.5|x2|
|`FireType`|x2|x1|x0.5|
|`WaterType`|x0.5|x2|x1|

**Pueden agregar otras cosas que necesiten para que la clase funcione.** ¡Piensen que cosas van a la clase padre!

#### TESTS

Para verificar que este punto esté bien pueden correr

```python -m pytest tests.py::TestAttack```

### Punto 3 - Batallas

Ahora si, los vamos a hacer pelear. Completar la función `pokemon_battle` (en el archivo `battle.py`) que toma 2 pókemon y los hace pelear hasta que uno gana. ¿Qué implica una pelea? Implica que se atacan de a turnos hasta que alguno se desmaya. Comienza el primer pokémon pasado por parámetro. La función retorna el pokémon ganador (el pokémon entero, no sólo el nombre). Pueden meter prints en el medio para que vean como está funcionando.

#### TESTS

Para verificar que este punto esté bien pueden correr

```python -m pytest tests.py::TestBattle```

