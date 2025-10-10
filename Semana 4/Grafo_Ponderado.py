import networkx as nx
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
G = nx.DiGraph()

G.add_nodes_from(["Habitaciones", "Social","Seguridad", "Recepcion", "Parqueo", "Servicio","Almacen"])

# Añadir aristas con pesos
G.add_edge('Habitaciones', 'Social', weight=4)
G.add_edge('Habitaciones', 'Seguridad', weight=2)
G.add_edge('Habitaciones', 'Recepcion', weight=4)
G.add_edge('Habitaciones', 'Parqueo', weight=3)
G.add_edge('Habitaciones', 'Servicio', weight=6)
G.add_edge('Habitaciones', 'Almacen', weight=7)
G.add_edge('Seguridad', 'Social', weight=5)
G.add_edge('Recepcion', 'Parqueo', weight=8)
G.add_edge('Servicio', 'Parqueo', weight=8)
G.add_edge('Servicio', 'Almacen', weight=8)

print("Grafo dirigido:")
print(G.edges(data=True)) # Muestra las aristas con sus pesos

pos = nx.spring_layout(G)

# Dibujar nodos y arcos
nx.draw_circular(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)

# Extraer las etiquetas de los arcos
edge_labels = nx.get_edge_attributes(G, 'weight')

# Dibujar las etiquetas en los arcos
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.show()