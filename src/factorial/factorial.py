#/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0:  # verifica si el número es negativo
        print("Factorial de un número negativo no existe")
    elif num == 0: # retorna 1 si el número es cero
        return 1  
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1: # verifica si no se proporcionaron argumentos de línea de comandos
    rango = input("Ingrese el rango (sin límite inferior -hasta o sin límite superior desde-): ")
    if rango.startswith("-"):  # si el rango comienza con "-", establece el límite superior y deja el inferior en 1
        hasta = int(rango[1:])  
        hasta = int(rango[1:])
        desde = 1
    elif rango.endswith("-"):  # si el rango termina con "-", establece el límite inferior y el superior en 60
        desde = int(rango[:-1])
        hasta = 60
    else:                      # si el rango está en formato "desde-hasta", divide el rango y establece los límites
        desde, hasta = map(int, rango.split('-'))
else:                          # si se proporcionaron argumentos de línea de comandos
    rango = sys.argv[1]
    if rango.startswith("-"):
        hasta = int(rango[1:])
        desde = 1
    elif rango.endswith("-"):
        desde = int(rango[:-1])
        hasta = 60
    else:
        desde, hasta = map(int, rango.split('-'))

for num in range(desde, hasta + 1):   # bucle sobre el rango especificado
    print("Factorial", num, "! es", factorial(num))  # imprime el factorial de cada número en el rango
