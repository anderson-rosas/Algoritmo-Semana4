# Llenar la pila con 15 números
pila1 = []
pila2 = []

for i in range(1, 16):
    pila1.append(i)

print("Pila inicial:", pila1)

# Usar pop para eliminar el séptimo (índice 6) y luego el tercero (índice 2)
pila2.append(pila1.pop(6))  # Elimina y guarda el séptimo elemento
pila2.append(pila1.pop(2))  # Elimina y guarda el tercer elemento

print("Pila después de eliminar el tercer y séptimo elemento:", pila1)
print("Elementos eliminados (guardados en pila2):", pila2)
