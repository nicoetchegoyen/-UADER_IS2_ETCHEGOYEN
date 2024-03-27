#/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* Calcula la secuencia de números de Collatz y grafica los resultados     *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    x_values = [] 
    y_values = []

    for n in range(1, 10001):
        sequence = collatz_sequence(n)
        x_values.append(len(sequence) - 1)
        y_values.append(n)

    plt.scatter(x_values, y_values, s=5, color='red')
    plt.title('Número de iteraciones de Collatz para números entre 1 y 10000')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número inicial de la secuencia (n)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
