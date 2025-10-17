import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # Para visualización

# Crear un grafo no dirigido
g = nx.Graph()

# Leer aristas desde archivo txt
edges = []
with open("tabla.txt", "r") as file:
    for line in file:
        u, v, w = line.strip().split()
        edges.append((u, v, int(w)))

# Agregar aristas al grafo
g.add_weighted_edges_from(edges)

# Usar un layout que minimiza cruces de aristas
pos = nx.kamada_kawai_layout(g)

# Crear subplots para comparar los grafos
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 6)

# Etiquetas de los pesos
labels = nx.get_edge_attributes(g, 'weight')

# Dibuja el grafo original
ax[0].set_title('Gráfica original')
nx.draw_kamada_kawai(g, with_labels=True, node_color='#bbbb22', node_size=500, ax=ax[0])
nx.draw_networkx_edge_labels(g, pos, ax=ax[0], edge_labels=labels)

# Aplicar Prim para obtener el árbol de expansión mínima
mst = nx.minimum_spanning_tree(g, algorithm='prim')
labels_mst = nx.get_edge_attributes(mst, 'weight')

# Dibuja el árbol de peso mínimo
ax[1].set_title('Árbol de peso mínimo (Prim)')
nx.draw(mst, pos, with_labels=True, node_color='#22bbbb', node_size=500, ax=ax[1])
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels_mst, ax=ax[1])

plt.tight_layout()
plt.show()
