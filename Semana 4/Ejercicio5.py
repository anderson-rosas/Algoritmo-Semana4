#pila para 20 nombre e imprimir usando el concepto LIFO

pila1=[]
pila2=[]

for i in range(1,21):
    nom=input("Ingresar nombre: ")
    pila1.append(nom)

print("Pila inicial de nombres: ",pila1)

pila2.append(pila1.pop())
print("Ultimo nombre es: ",pila2)
print("Pila inicial sin el ultimo nombre: ",pila1)