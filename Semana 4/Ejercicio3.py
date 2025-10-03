import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()
g.add_edge("A","B",relation="amigo")
g.add_edge("B","C",relation="trabajo")
g.add_edge("C","D",relation="amigo")
g.add_edge("A","D",relation="trabajo")

pos = nx.spring_layout(g)

# Dibujar nodos y aristas
plt.figure(figsize=(8, 6))
nx.draw(g, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12, arrows=True)

edge_labels = nx.get_edge_attributes(g, 'relation')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')
# Dibujar el grafo

plt.show() # Muestra el gráfico