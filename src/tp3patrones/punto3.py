"""Genere una clase donde se instancie una comida rápida “hamburguesa” que
pueda ser entregada en mostrador, retirada por el cliente o enviada por
delivery. A los efectos prácticos bastará que la clase imprima el método de
entrega"""

from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def crear_hamburguesa(self):
        pass

class MostradorHamburguesa(Creator):
    def crear_hamburguesa(self):
        return HamburguesaMostrador()

class DeliveryHamburguesa(Creator):
    def crear_hamburguesa(self):
        return HamburguesaDelivery()

class ClienteHamburguesa(Creator):
    def crear_hamburguesa(self):
        return HamburguesaCliente()

class hamburguesa(ABC):
    def operation(self) -> str:
        return "hamburguesa"
    
class HamburguesaMostrador(hamburguesa):
    def __str__(self):
        return "hamburguesa entregada en mostrador"

class HamburguesaDelivery(hamburguesa):
    def __str__(self):
        return "hamburguesa entregada por delivery"

class HamburguesaCliente(hamburguesa):
    def __str__(self):
        return "hamburguesa retirada por el cliente"

def entregar_hamburguesa(factory):
    hamburguesa = factory.crear_hamburguesa()
    print("-------------------------------------------------------------")
    print("ESTADO DE ENTREGA:", hamburguesa)

if __name__ == "__main__":
    entregar_hamburguesa(MostradorHamburguesa())
    entregar_hamburguesa(DeliveryHamburguesa())
    entregar_hamburguesa(ClienteHamburguesa())
