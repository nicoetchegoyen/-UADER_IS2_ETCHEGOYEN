"""1. Cree una clase bajo el patrón cadena de responsabilidad donde los números del
1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que
identifique la necesidad de consumir el número lo hará y caso contrario lo
pasará al siguiente en la cadena. Implemente una clase que consuma números
primos y otra números pares. Puede ocurrir que un número no sea consumido
por ninguna clase en cuyo caso se marcará como no consumido."""

import os

class Handler(object):
    def __init__(self):
        self.next_handler = None

    def handle(self, number):
        if self.next_handler == None:
            print("numero {} no consumido.".format(number))
            return
        self.next_handler.handle(number)
 
class PrimoHandler(Handler):
    def handle(self, number):
        if self.is_prime(number):
            print("numero primo encontrado: {}".format(number))
        else:
            super().handle(number)

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

class ParHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print("numero par encontrado: {}".format(number))
        else:
            super().handle(number)

class ImparHandler(Handler):
    def handle(self, number):
        if number % 2 != 0:
            print("numero impar encontrado: {}".format(number))
        else:
            super().handle(number)

def build_chain():
    primo_handler = PrimoHandler()
    par_handler = ParHandler()
    impar_handler = ImparHandler()

    primo_handler.next_handler = par_handler
    par_handler.next_handler = impar_handler

    return primo_handler

if __name__ == "__main__":
    os.system("cls")
    print("Ejemplo de cadena de responsabilidad para manejar números primos, pares e impares.\n")

    chain = build_chain()

    for number in range(1, 101):
        chain.handle(number)
