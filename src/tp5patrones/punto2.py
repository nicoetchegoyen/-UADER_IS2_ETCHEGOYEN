"""2. Implemente una clase bajo el patrón iterator que almacene una cadena de
caracteres y permita recorrerla en sentido directo y reverso."""

class Iterator:
    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._index = 0 if not reverse else len(collection) - 1
        self._step = 1 if not reverse else -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0 or self._index >= len(self._collection):
            print("<eol>")
            raise StopIteration
        result = self._collection[self._index]
        self._index += self._step
        return result    

class Collection:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator(self._items)

    def add_item(self, item):
        self._items.append(item)

    def reverse_iterator(self):
        return Iterator(self._items, reverse=True)


collection = Collection()
collection.add_item('a')
collection.add_item('b')
collection.add_item('c')

print("recorrido en sentido directo:")
for item in collection:
    print(item)

print("recorrido en sentido inverso:")
reverse_iter = collection.reverse_iterator()
for item in reverse_iter:
    print(item)
