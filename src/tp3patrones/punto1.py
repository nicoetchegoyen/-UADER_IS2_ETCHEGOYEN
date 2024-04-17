""". Provea una clase que dado un número entero cualquiera retorne el factorial del
mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
instancia de clase."""
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Factorial(metaclass=SingletonMeta):
    def __init__(self):
        pass

    def calcular_factorial(self, n):
        if n < 0:
            print("inserte un numero positivo")
        if n == 0:
            return 1
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

if __name__ == "__main__":

    f1 = Factorial()
    f2 = Factorial()

    if id(f1) == id(f2):
        print("factorial de 5:", f1.calcular_factorial(5))
        print("factorial de 10:", f1.calcular_factorial(10))
