#/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
    rango = input("Ingrese el rango (sin límite inferior -hasta o sin límite superior desde-): ")
    if rango.startswith("-"):
        hasta = int(rango[1:])
        desde = 1
    elif rango.endswith("-"):
        desde = int(rango[:-1])
        hasta = 60
    else:
        desde, hasta = map(int, rango.split('-'))
else:
    rango = sys.argv[1]
    if rango.startswith("-"):
        hasta = int(rango[1:])
        desde = 1
    elif rango.endswith("-"):
        desde = int(rango[:-1])
        hasta = 60
    else:
        desde, hasta = map(int, rango.split('-'))

for num in range(desde, hasta + 1):
    print("Factorial", num, "! es", factorial(num))
