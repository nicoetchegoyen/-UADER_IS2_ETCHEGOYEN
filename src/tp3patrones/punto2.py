"""Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
deberá recibir un valor de importe base imponible y deberá retornar la suma
del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
esa base imponible."""

class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class CalculadoraImpuestos(metaclass=SingletonMeta):
    def __init__ (self):
        pass

    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        cont_municipales = base_imponible * 0.012
        total_impuestos = iva + iibb + cont_municipales
        return total_impuestos


if __name__ == "__main__":

    calculadora1 = CalculadoraImpuestos()
    calculadora2 = CalculadoraImpuestos()
    if id(calculadora1) == id(calculadora2):
        print("Total de impuestos a pagar:", calculadora1.calcular_impuestos(1000))
        print("Total de impuestos a pagar:", calculadora1.calcular_impuestos(56250))
        print("Total de impuestos a pagar:", calculadora1.calcular_impuestos(9121))
    
    
