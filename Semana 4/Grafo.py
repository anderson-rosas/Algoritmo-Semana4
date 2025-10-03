import networkx as nx
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo no dirigido
G = nx.DiGraph()


# Añadir nodos individuales
G.add_node("A")
G.add_node("B")
#Añadir aristas individuales
G.add_edge("A", "B")
G.add_edge("B", "C")
#Añadir multiples aristas desde una lista de tuplas
G.add_edges_from([("C","D"),("D","E"),("E","A"),("A","B"),("B","C")])
# dibujar el grafo
nx.draw(G, with_labels=True)
plt.show() # Muestra el gráfico