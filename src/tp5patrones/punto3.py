"""3. Implemente una clase bajo el patrón observer donde una serie de clases están
subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4
caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio
coinciden. Implemente 4 clases de tal manera que cada una tenga un ID
especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con
ID para el que tenga una clase implementada."""

import os

class Subject:
    def __init__(self):
        self._observers = []

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

class Data(Subject):
    def __init__(self, name=''):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        print("El dato bajo observación ha sido actualizado al valor %d\n" % (value))
        self.notify()


class Observer:
    def update(self, subject):
        pass

class IDObserver(Observer):
    def __init__(self, observer_id):
        self.id = observer_id

    def update(self, subject):
        if self.id == subject.name:
            print(f"se recibio una actualizacion con el ID coincidente: {subject.name}")


if __name__ == "__main__":
    os.system("clear")

    print("crea los observadores para IDs específicos\n")
    observer1 = IDObserver('ASDF')
    observer2 = IDObserver('ZXCV')
    observer3 = IDObserver('1234')
    observer4 = IDObserver('5678')

    print("\ncrea un objeto de datos, suscribe los observadores\n")
    obj1 = Data('ASDF')
    obj1.attach(observer1)
    obj1.attach(observer2)
    obj1.attach(observer3)
    obj1.attach(observer4)

    print("modifica el dato")
    obj1.data = 10

    print("\ncrea otro objeto de datos, suscribe los observadores\n")
    obj2 = Data('ZXCV')
    obj2.attach(observer1)
    obj2.attach(observer2)
    obj2.attach(observer3)
    obj2.attach(observer4)

    print("modifica el dato")
    obj2.data = 15
