#*-------------------------------------------------------------------------
#* prototipo.py
#* Ejemplo para creación de prototipos
#*-------------------------------------------------------------------------
"""6. Extienda el ejemplo del taller para prototipos de forma que genere 20
anidamientos y que la carga simulada de procesamiento dure 2 segundos."""
from abc import ABC, abstractmethod
import time
from datetime import datetime
import copy
import os


# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(3)
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

#*------------------------------------------------------------------------------
#* El método clone() no está definido en el prototipo y mediante @abstractmethod
#* se fuerza a que cualquier instancia que se haga de ésta clase lo tenga que
#* definir.
#*------------------------------------------------------------------------------
    # Clone Method:
    @abstractmethod
    def clone(self):
        pass 

#*------------------------------------------------------------------------------
#* Clase productiva que puedo querer usar como plantilla
#*------------------------------------------------------------------------------
class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30


    # Implementa el método de clonado mediante una copia de arbol de métodos
    def clone(self):
        return copy.deepcopy(self)    

#*-------------------------------------------------------------------------
#* clase 
#* define un atributo específico
#*-------------------------------------------------------------------------
class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.stamina = 60
    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)  

#*--------------------------------------------------------------------------
class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
    # Call superclass constructor, time.sleep() and assign base values
        self.mana = 100

    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self) 

#*--------------------------------------------------------------------------
#* Punto de entrada de ejecución
#*--------------------------------------------------------------------------

os.system("clear")

dt = datetime.now()
print('comienzo creando un objeto shopkeeper NPC: ', dt)
shopkeeper = Shopkeeper(180, 22, 5, 8)

dt = datetime.now()
print('finaliza la creación del objeto shopkeeper NPC: ', dt)
print('atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))


for i in range(20):
    dt = datetime.now()
    print(f'creando shopkeeper NPC anidado {i + 1}...', dt)
    shopkeeper = shopkeeper.clone()
    time.sleep(2)
    dt = datetime.now()
    print(f'finalizado shopkeeper NPC anidado {i + 1}.', dt)

dt = datetime.now()
print('finalizo la creación de los anidamientos.', dt)

