class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.queue = [None] * capacidad
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.capacidad == self.front

    def enqueue(self, element):
        if self.isFull():
            return "La cola está llena"
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacidad
        self.queue[self.rear] = element

    def dequeue(self):
        if self.isEmpty():
            return "La cola está vacía"
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacidad
        return removed

    def peek(self):
        if self.isEmpty():
            return "La cola está vacía"
        return self.queue[self.front]

    def size(self):
        if self.isEmpty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacidad - self.front + self.rear + 1

    def mostrar(self):
        if self.isEmpty():
            return []
        elementos = []
        i = self.front
        while True:
            elementos.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacidad
        return elementos

    def mostrar_extremos(self):
        if self.isEmpty():
            print("La cola está vacía")
        else:
            print("Primer elemento (front):", self.queue[self.front])
            print("Último elemento (rear):", self.queue[self.rear])


# 🧪 Prueba
miColaCircular = ColaCircular(5)

miColaCircular.enqueue('Nestor')
miColaCircular.enqueue('Ana')
miColaCircular.enqueue('Carlos')

print("Cola: ", miColaCircular.mostrar())
miColaCircular.mostrar_extremos()

print("Elimina: ", miColaCircular.dequeue())
print("Cola después de eliminar: ", miColaCircular.mostrar())
miColaCircular.mostrar_extremos()

miColaCircular.enqueue('Selena')
miColaCircular.enqueue('Nathan')

print("Cola después de agregar más elementos: ", miColaCircular.mostrar())
miColaCircular.mostrar_extremos()