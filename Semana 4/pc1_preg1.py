class Nodo:
    def __init__(self, codigo, nombre, hora_inicio):
        self.codigo = codigo
        self.nombre = nombre
        self.hora_inicio = hora_inicio

    def info(self):
        return f"Curso: {self.codigo} | Código: {self.nombre} | Hora: ({self.hora_inicio})"

# Lista de nodos (cursos)
cursos = [
    Nodo("EST101", "ESTADISTICA Y PROBABILIDADES II", "14:00"),
    Nodo("FIS202", "FÍSICA II", "10:30"),
    Nodo("TEC305", "TECNOLOGIA DE INFORMACIÓN II", "09:15"),
    Nodo("AED110", "ALGORITMO Y ESTRUCTURA DE DATOS II", "16:45"),
    Nodo("MIC150", "MICROECONOMÍA", "12:00")
]

def mergeSort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = mergeSort(lista[:medio])# elementos de la parte izquierda de la lista
        derecha = mergeSort(lista[medio:])# elementos de la parte derecha de la lista
        return merge(izquierda, derecha)
    else:
        return lista

def merge(izquierda, derecha):
    resultado = [] #Aqui se guarda la lista ordenada
    i = 0
    j = 0 

    while i < len(izquierda) and j < len(derecha): #Mientras haya elementos en las 2 listas 
        if izquierda[i].hora_inicio <= derecha[j].hora_inicio:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes de izquierda
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Agregar los elementos restantes de derecha
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

def buscarCursoPorHora(lista, hora):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio].hora_inicio == hora:
            return lista[medio]
        elif hora < lista[medio].hora_inicio:
            fin = medio - 1
        else:
            inicio = medio + 1
    return None

def poblar():
    r="s"
    while r=="s":
        codigo=input("Ingrese el código del curso: ")
        nombre=input("Nombre del curso: ").upper()
        hora=input("Hora de inicio (HH:MM): ")
        cursos.append(Nodo(codigo, nombre, hora))
        r=input("Desea seguir ingresando datos? [S/N] : ").lower()

poblar()
# Mostrar antes de ordenar
print("Cursos antes de ordenar:")
for i in range(len(cursos)):
    print(cursos[i].info())

# Ordenar
cursos_ordenados = mergeSort(cursos)

print("\nCursos después de ordenar:")
for i in range(len(cursos_ordenados)):
    print(cursos_ordenados[i].info())

# Buscar por hora
hora_buscada = input("Ingrese la hora a buscar: ")
curso_encontrado = buscarCursoPorHora(cursos_ordenados, hora_buscada)

print(f"\nBuscando el horario con la hora buscada:")
if curso_encontrado:
    print(curso_encontrado.info())
else:
    print("No se encontró ningún curso con esa hora.")