#/usr/bin/python3
# Python program to display all the prime numbers within an interval
# Definir el rango de números para encontrar los números primos
lower = 1
upper = 100

# Imprimir el mensaje indicando el rango de números
print("Números primos entre", lower, "y", upper, "son:")

# Iterar a través de cada número en el rango especificado
for num in range(lower, upper + 1):
   # Verificar si el número es mayor que 1, ya que todos los números primos son mayores que 1
   if num > 1:
       # Iterar a través de los números desde 2 hasta num - 1 para verificar si num es divisible por algún número anterior
       for i in range(2, num):
           # Si num es divisible por algún número en el rango, no es primo, entonces salimos del bucle interno
           if (num % i) == 0:
               break
       else:
           # Si no encontramos ningún divisor para num, significa que num es primo y lo imprimimos
           print(num)

