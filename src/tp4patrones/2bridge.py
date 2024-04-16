# Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
# dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
# de 10 mts. Genere una clase que represente a las láminas en forma genérica al
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
# patrón bridge en la solución)

class LaminaAcero:
    def __init__(self, espesor, ancho, laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.laminador = laminador

class ProducingLaminas:
    def producir(self, espesor, ancho):
        pass

class ProducingLam5M(ProducingLaminas):
    def producir(self, espesor, ancho):
        print(f"laminador de 5 metros produciendo lamina de {espesor}\" de espesor y {ancho} metros de ancho.")

class ProducingLam10M(ProducingLaminas):
    def producir(self, espesor, ancho):
        print(f"laminador de 10 metros produciendo lamina de {espesor}\" de espesor y {ancho} metros de ancho.")

if __name__ == "__main__":

    producing_lam_5m = ProducingLam5M()
    producing_lam_10m = ProducingLam10M()

    print("\nproduccion de lamina de acero de 5 metros:")
    print ("---------------------------------------------------------------------------------------------")
    producing_lam_5m.producir(0.5, 1.5)
    
    print("\nproduccion de lamina de acero de 10 metros:")
    print ("---------------------------------------------------------------------------------------------")
    producing_lam_10m.producir(0.5, 1.5)
