# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para representar la red semántica
red_semantica = nx.DiGraph()

# Agregar nodos (conceptos)
red_semantica.add_node("Perro")
red_semantica.add_node("Gato")
red_semantica.add_node("Animal")
red_semantica.add_node("Mamífero")

# Agregar relaciones (aristas) entre los conceptos
red_semantica.add_edge("Perro", "Animal")
red_semantica.add_edge("Gato", "Animal")
red_semantica.add_edge("Animal", "Mamífero")

# Dibujar la red semántica
pos = nx.spring_layout(red_semantica)
nx.draw(red_semantica, pos, with_labels=True, node_size=1000, node_color="lightblue")
plt.title("Red Semántica")
plt.show()

# Consultar relaciones
relaciones = red_semantica.in_edges("Animal", data=True)
for origen, destino, datos in relaciones:
    print(f"Relación entre {origen} y {destino}: {datos.get('relation', 'Desconocida')}")
