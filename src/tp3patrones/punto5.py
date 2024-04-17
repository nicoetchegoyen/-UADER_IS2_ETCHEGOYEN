import os
"""Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar
para construir aviones en lugar de vehículos. Para simplificar suponga que un
avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje."""

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getAvion(self):
        avion = Avion()
        
        body = self.__builder.getBody()
        avion.setBody(body)

        for _ in range(2):
            turbina = self.__builder.getTurbina()
            avion.setTurbinas(turbina)

        for _ in range(2):
            wing = self.__builder.getAla()
            avion.setAlas(wing)

        tren_aterrizaje = self.__builder.getTrenAterrizaje()
        avion.setTrenAterrizaje(tren_aterrizaje)

        return avion

class Avion: 

    def __init__(self):
        self.__turbinas = list()
        self.__alas = list()
        self.__body = None
        self.__tren_aterrizaje = None
   
    def setBody(self, body):
        self.__body = body

    def setTurbinas(self, turbina):
        self.__turbinas.append(turbina)

    def setAlas(self, ala):
        self.__alas.append(ala)

    def setTrenAterrizaje(self, tren_aterrizaje):
        self.__tren_aterrizaje = tren_aterrizaje

    def specification(self):
        print("cuerpo:", self.__body.shape)
        print("turbinas:", len(self.__turbinas))
        print("alas:", len(self.__alas))
        print("tren de aterrizaje:", self.__tren_aterrizaje.type)
        
class Builder:
	
      def getBody(self): pass
      def getTurbina(self): pass
      def getAla(self): pass
      def getTrenAterrizaje(self): pass


class AvionBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "airbong"
        return body

    def getTurbina(self):
        turbina = Turbina()
        return turbina

    def getAla(self):
        ala = Ala()
        return ala

    def getTrenAterrizaje(self):
        tren_aterrizaje = TrenAterrizaje()
        tren_aterrizaje.type = "disponibles"
        return tren_aterrizaje

class Body:
    pass
 
class Turbina:
    pass

class Ala:
    pass

class TrenAterrizaje:
    pass


def main():
    avion_builder = AvionBuilder()
    director = Director()
    director.setBuilder(avion_builder)
    avion = director.getAvion() 
    avion.specification()

if __name__ == "__main__":
   main()
   


