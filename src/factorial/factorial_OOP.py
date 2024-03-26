#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* calcula el factorial de un número utilizando programación orientada a    *
#* objetos                                                                 *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

class Factorial:
    def __init__(self):
        pass 

    def factorial(self, num):
        if num < 0:
            print("el factorial de un numero negativo no existe")
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        for num in range(min, max + 1):
            print("Factorial", num, "! es", self.factorial(num))

if __name__ == "__main__":
    min_value = int(input("Ingrese el valor mínimo del rango: "))
    max_value = int(input("Ingrese el valor máximo del rango: "))

    factorial_calculator = Factorial()
    factorial_calculator.run(min_value, max_value)
