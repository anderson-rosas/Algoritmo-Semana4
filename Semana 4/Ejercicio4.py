import networkx as nx # type: ignore
import matplotlib.pyplot as plt # Para visualización
# Crear un grafo dirigido
g = nx.DiGraph()
g.add_edge("Lima", "Trujillo", relation="560Km")
g.add_edge("Trujillo", "Cajamarca", relation="300Km")
g.add_edge("Cajamarca", "Amazonas",relation="230Km")
g.add_edge("Amazonas", "Chiclayo",relation="797Km")
g.add_edge("Chiclayo", "Lima",relation="777Km")

pos=nx.spring_layout(g)
# Dibujar nodos y aristas
plt.figure(figsize=(8, 6))
nx.draw(g, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12, arrows=True)

edge_labels = nx.get_edge_attributes(g, 'relation')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')
# Dibujar el grafo

def calcular_galones_consumidos(grafo):
    total_km = 0
    for u, v, datos in grafo.edges(data=True):
        distancia_str = datos.get("relation", "0Km")
        km = int(distancia_str.replace("Km", ""))
        total_km += km
    galones = 0.102 * total_km
    print(f"Distancia total recorrida: {total_km} Km")
    print(f"Galones consumidos: {galones:.2f} galones")
    return galones
calcular_galones_consumidos(g)
plt.show()

