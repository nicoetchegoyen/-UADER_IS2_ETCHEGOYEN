# 1. Provea una clase ping que luego de creada al ser invocada con un método
# “execute(string)” realice 10 intentos de ping a la dirección IP contenida en
# “string” (argumento pasado), la clase solo debe funcionar si la dirección IP
# provista comienza con “192.”. Provea un método executefree(string) que haga
# lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
# cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
# www.google.com usando el método executefree de ping y re-envie a execute
# de la clase ping en cualquier otro caso. (Modele la solución como un patrón
# proxy)

import os

class PingBase:
    def execute(self, ip_address):
        pass

class Ping(PingBase):
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                response = os.system("ping -c 1" + ip_address)
                if response == 0:
                    print(ip_address, 'is up!')
                else:
                    print(ip_address, 'is down!')

class PingProxy(PingBase):
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.execute_free("www.google.com")
        else:
            print("proporcione una direccion valida")

    def execute_free(self, address):
        for _ in range(10):
            response = os.system("ping -c 1 " + address)
            if response == 0:
                print(address, 'en linea')
            else:
                print(address, 'error')

if __name__ == "__main__":
    print("testeando Ping:")
    ping = Ping()
    ping.execute("192.168.1.1")

    print("\n testeando PingProxy:")
    proxy = PingProxy()
    proxy.execute("192.168.1.1")
    proxy.execute("192.168.0.254")
    proxy.execute("190.999.9.999")
