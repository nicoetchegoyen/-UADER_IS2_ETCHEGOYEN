# . Represente la lista de piezas componentes de un ensamblado con sus
# relaciones jerárquicas. Empiece con un producto principal formado por tres
# sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
# que representen esa configuración y la muestren. Luego agregue un subconjunto 
# opcional adicional también formado por cuatro piezas. (Use el patrón
# composite).

class Component:
    def showDetails(self):
        pass

class Pieza(Component):
    def __init__(self, nombre):
        self.nombre = nombre

    def showDetails(self):
        print(f"  - {self.nombre}")

class Ensamblado(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self.children = []

    def add(self, child):
        self.children.append(child)

    def showDetails(self):
        print(f"{self.nombre}:")
        for child in self.children:
            child.showDetails()

if __name__ == "__main__":
    pieza1 = Pieza("Pieza 1")
    pieza2 = Pieza("Pieza 2")
    pieza3 = Pieza("Pieza 3")
    pieza4 = Pieza("Pieza 4")
    pieza5 = Pieza("Pieza 5")
    pieza6 = Pieza("Pieza 6")
    pieza7 = Pieza("Pieza 7")
    pieza8 = Pieza("Pieza 8")
    pieza9 = Pieza("Pieza 9")
    pieza10 = Pieza ("Pieza 10")
    pieza11 = Pieza ("Pieza 11")
    pieza12 = Pieza ("Pieza 12")
    
    topLevel = Ensamblado("Producto Principal")
    subItem1 = Ensamblado("Sub-Conjunto 1")
    subItem2 = Ensamblado("Sub-Conjunto 2")
    subItem3 = Ensamblado("Sub-Conjunto 3")
    subconjuntoOpcional = Ensamblado("Sub-Conjunto Opcional")

    subItem1.add(pieza1)
    subItem1.add(pieza2)
    subItem1.add(pieza3)
    subItem1.add(pieza4)

    subItem2.add(pieza5)
    subItem2.add(pieza6)
    subItem2.add(pieza7)
    subItem2.add(pieza8)

    subItem3.add(pieza9)
    subItem3.add(pieza10)
    subItem3.add(pieza11)
    subItem3.add(pieza12)

    topLevel.add(subItem1)
    topLevel.add(subItem2)
    topLevel.add(subItem3)

    topLevel.add(subconjuntoOpcional)

    topLevel.showDetails()
