import random
pilaFia = []
pilaFia2 = []

# Push inicial
for i in range (1,16):
    pilaFia.append(i)

print("Pila inicial:", pilaFia)

sacarD = int(input("Ingrese el numero a buscado: "))
temp = 0

# Sacar elementos hasta encontrar el número deseado
while pilaFia:
    temp = pilaFia.pop()
    if temp == sacarD:
        print(f"¡Número {sacarD} eliminado!")
        break
    else:
        pilaFia2.append(temp)

print("Pila después de eliminar el número:", pilaFia)
print("Elementos guardados temporalmente:", pilaFia2)

# Restaurar los elementos en el orden original
while pilaFia2:
    pilaFia.append(pilaFia2.pop())

print("Pila restaurada (sin el número eliminado):", pilaFia)