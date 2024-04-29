"""5. Modifique el programa IS2_taller_memory.py para que la clase tenga la
capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los
mismos en cualquier orden de ser necesario. El método undo deberá tener un
argumento adicional indicando si se desea recuperar el inmediato anterior (0) y
los anteriores a el (1,2,3)."""
import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:
            del self.history[0]


    def undo(self, steps=1):
        for _ in range(steps):
            if self.history:
                memento = self.history.pop()
                self.file = memento.file
                self.content = memento.content


class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps=1):
        writer.undo(steps)

if __name__ == '__main__':
    os.system("cls")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)
    
    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)
    
    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)


    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar 4 estados anteriores")
    caretaker.undo(writer, 4)
    
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
