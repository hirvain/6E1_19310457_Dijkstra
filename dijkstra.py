# -*- coding: utf-8 -*-
"""
Created on Wed May 18 02:59:32 2022

@author: Equipo
"""
import networkx as nx
import matplotlib.pyplot as plt
import random

pesos = [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)]


Grafo = nx.Graph()
Grafo.add_node("A")      
Grafo.add_node("E")
Grafo.add_node("I")
Grafo.add_node("O")
Grafo.add_node("U")
Grafo.add_edge("A","E", weight=pesos[0], color='b')  
Grafo.add_edge("E","I", weight=pesos[1], color='b')
Grafo.add_edge("O","A", weight=pesos[2], color='b')
Grafo.add_edge("O","U", weight=pesos[3], color='b')
Grafo.add_edge("I","U", weight=pesos[4], color='b')
Grafo.add_edge("E","U", weight=pesos[5], color='b')
Grafo.add_edge("E","O", weight=pesos[6], color='b')

#camino = nx.dijkstra_path(Grafo, source='U', target = 'I', weight = True)
length,camino=nx.bidirectional_dijkstra(Grafo,'U','I') #Siempre usar bidirectional_dijkstra

for i in range(len(camino)-1):
    Grafo.add_edges_from ([(camino[i],camino[i+1])], color = 'red')
    
colors = nx.get_edge_attributes(Grafo,'color').values()

pos = nx.spring_layout(Grafo)
plt.figure()


nx.draw(
    Grafo, pos, edge_color=colors, width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in Grafo.nodes()}
)

nx.draw_networkx_edge_labels(
    Grafo, pos,
    edge_labels={('A', 'E'): pesos[0],
                 ('E', 'I'): pesos[1], 
                 ('O', 'A'): pesos[2],
                 ('O', 'U'): pesos[3],
                 ('I', 'U'): pesos[4],
                 ('E', 'U'): pesos[5],
                 ('E', 'O'): pesos[6], 
                 
                 },
    font_color='red'
)

print(camino)
