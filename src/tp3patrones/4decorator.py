# Implemente una clase que permita a un número cualquiera imprimir su valor,
# luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a
# las clases con las diferentes operaciones. Use un patrón decorator para
# implementar.

class Componente:
    def operacion(self):
        pass

class Numero(Componente):
    def __init__(self, value):
        self.value = value

    def operacion(self):
        return self.value

class Decorator(Componente):
    def __init__(self, componente):
        self.componente = componente

    def operacion(self):
        return self.componente.operacion()

class MasDos(Decorator):
    def operacion(self):
        return self.componente.operacion() + 2

class Por2(Decorator):
    def operacion(self):
        return self.componente.operacion() * 2

class Dividido3(Decorator):
    def operacion(self):
        return self.componente.operacion() / 3


if __name__ == "__main__":
    numero = Numero(5)

    print("---------------------------------------------------------------")
    print("numero:", numero.operacion())

    suma2 = MasDos(numero)
    multiplica2 = Por2(numero)
    divide3 = Dividido3(numero)

    print("numero mas 2:", suma2.operacion())
    print("numero multiplicado por 2:", multiplica2.operacion())
    print("numero dividido 3:", divide3.operacion())
    print("---------------------------------------------------------------")
