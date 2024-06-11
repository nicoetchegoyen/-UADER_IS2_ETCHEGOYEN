# -----------------------------------------------------------------------------
# Copyright UADERFCyT-IS2©2024 todos los derechos reservados.
# -----------------------------------------------------------------------------
# Este programa lee un archivo JSON y devuelve el valor del token requerido.
# Estrategia Branching by abstraction
# Patron Singleton
# Cadena de comando
# V1.2
# get_jason.py
# python 3.12.0
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod
import sys
import json
from collections.abc import Iterator, Iterable

# caratula
print('*-----------------------------------------------------------------------------*')
print('| Copyright UADERFCyT-IS2©2024 todos los derechos reservados.                 |')
print('*-----------------------------------------------------------------------------*')
#imprimir las instrucciones por si no se ejecuta desde la terminal y con los argumentos
print('*-----------------------------------------------------------------------------------------*')
print('|-Para conocer la versión del programa utilice get_jason.py -v                  |')
print('|-Para conocer su token utilice: python get_jason.py sitedata.json {nombredeltoken}|')
print('|-Para realizar un pago: python get_jason.py sitedata.json pagar {monto}        |')
print('*-----------------------------------------------------------------------------------------*')

# clase abstracta que define el contrato para obtener un valor de un archivo .json
class JSONHandler(ABC):
    @abstractmethod
    def get_value(self, jsonfile, jsonkey):
        pass

# implementacion refactorizada con y el patron singleton de la clase ABC JSONHandler
class SingletonJSONHandler(JSONHandler):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonJSONHandler, cls).__new__(cls)
        return cls._instance

    def get_value(self, jsonfile, jsonkey):
# intenta abrir el archivo .json
        try:
            with open(jsonfile, 'r', encoding='utf-8') as myfile:
                data = myfile.read()
# si el archivo no se encuentra, muestra un mensaje de error y termina el programa controladamente
        except FileNotFoundError:
            print(f"error: el archivo '{jsonfile}' no se encuentra.")
            sys.exit(1)

        try:
# convierte el contenido del archivo (cadena de texto) en un objeto JSON
            obj = json.loads(data)
# si el contenido no es un .json valido, muestra un mensaje de error y lo maneja controladamente
        except json.JSONDecodeError:
            print(f"error: el archivo '{jsonfile}' no es un JSON válido.")
            sys.exit(1)
# verifica si el token esta en el .json
        if jsonkey in obj:
            return str(obj[jsonkey])
        print(f"error: la clave '{jsonkey}' no existe en el JSON.")
        sys.exit(1)

# clase para iterar sobre los pagos realizados
class PagoIterator(Iterator):
    def __init__(self, pagos):
        self._pagos = pagos
        self._index = 0

    def __next__(self):
        if self._index < len(self._pagos):
            result = self._pagos[self._index]
            self._index += 1
            return result
        raise StopIteration

# clase para manejar los pagos
class PagoHandler(Iterable):
    def __init__(self, json_handler):
        self.saldos = {
            "token1": 1000,
            "token2": 2000
        }
        self.json_handler = json_handler
        self.pagos_realizados = []
        self.next_token = "token1"

    def pagar(self, monto, pedido):
 # intentar todas las cuentas
        for _ in range(len(self.saldos)):
            if self.saldos[self.next_token] >= monto:
                self.saldos[self.next_token] -= monto
                self.pagos_realizados.append((pedido, self.next_token, monto))
                print(f"pedido {pedido}: pago de ${monto} realizado desde la cuenta asociada a {self.next_token}. nuevo saldo: ${self.saldos[self.next_token]}")
# alternar el token para el siguiente pago
                self.next_token = "token2" if self.next_token == "token1" else "token1"
                return
            else:
# alternar el token para intentar con la otra cuenta
                self.next_token = "token2" if self.next_token == "token1" else "token1"

        print(f"pedido {pedido}: error: saldo insuficiente en ambas cuentas para realizar el pago de ${monto}.")

    def __iter__(self):
        return PagoIterator(self.pagos_realizados)

    def listar_pagos(self):
        print("listado de pagos realizados:")
        for idx, (pedido, token, monto) in enumerate(self, start=1):
            print(f"{idx}. pedido: {pedido}, token: {token}, monto: ${monto}")

def main():
# verificar los argumentos de entrada
    if len(sys.argv) < 3:
# para conocer la versión del programa
        if len(sys.argv) == 2 and sys.argv[1] == '-v':
            print("versión 1.2")
            sys.exit(0)
# si no se ingresaron los argumentos necesarios de entrada
        print("utilice: python get_jason.py sitedata.json {nombredeltoken}")
        sys.exit(1)

# almacena los argumentos pasados en variables
    jsonfile = sys.argv[1]

    json_handler = SingletonJSONHandler()
    pago_handler = PagoHandler(json_handler)

    if len(sys.argv) == 4 and sys.argv[2] == 'pagar':
        monto = float(sys.argv[3])
        pedido = len(pago_handler.pagos_realizados) + 1
        pago_handler.pagar(monto, pedido)
    else:
        jsonkey = sys.argv[2]
        value = json_handler.get_value(jsonfile, jsonkey)
        print(f'{jsonkey}: {value}')

    if len(pago_handler.pagos_realizados) > 0:
        pago_handler.listar_pagos()

# función principal
if __name__ == "__main__":
    main()
