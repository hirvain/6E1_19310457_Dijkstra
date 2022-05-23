# -*- coding: utf-8 -*-
"""
Created on Wed May 18 02:59:32 2022

@author: Oscar Antonio García Avila
"""
import networkx as nx
import random
import math
#                  0                      1                   2                   3                          4                      5                       6                         7                     8                       9                       10                        11                       12                    13                      14                      15
pesos = [random.randint(10, 20),random.randint(20, 60),random.randint(5, 10), random.randint(20, 30),random.randint(10, 30),random.randint(7, 12), random.randint(5, 10), random.randint(25, 40), random.randint(20, 30), random.randint(12, 20), random.randint(30, 50), random.randint(10, 20), random.randint(12, 20), random.randint(20, 30), random.randint(20, 30), random.randint(40, 60)]
vertices = ["Casa","Auto","C85-A","T18-A","Providencia","C135", "Americas", "R.Center", "C54", "C72", "T08", "N.Escocia", "Bicicleta", "CETI" ]
"""
0 Casa
1 Auto
2 C85-A
3 T18-A
4 Caminar desde Providencia
5 C135
6 Caminar desde Americas
7 Caminar a Real Center
8 C54
9 C72
10 T08
11 Caminar Nueva Escocia
12 Bicicleta
13 CETI
"""
Grafo = nx.Graph()
for i in range(12):
    Grafo.add_node(vertices[i])  

Grafo.add_edge(vertices[0],vertices[1], weight=1, color='b') 
Grafo.add_edge(vertices[1],vertices[13], weight=pesos[1], color='b') 


Grafo.add_edge(vertices[0],vertices[2], weight=pesos[2], color='b')
Grafo.add_edge(vertices[2],vertices[3], weight=pesos[3], color='b')
Grafo.add_edge(vertices[3],vertices[4], weight=pesos[4], color='b')
Grafo.add_edge(vertices[4],vertices[13],weight=pesos[5], color='b')

Grafo.add_edge(vertices[0],vertices[5], weight=pesos[6], color='b')
Grafo.add_edge(vertices[5],vertices[6], weight=pesos[7], color='b')
Grafo.add_edge(vertices[6],vertices[13],weight=pesos[8], color='b')


Grafo.add_edge(vertices[0],vertices[7], weight=1, color='b')
Grafo.add_edge(vertices[7],vertices[8], weight=pesos[9], color='b')
Grafo.add_edge(vertices[8],vertices[11], weight=pesos[10], color='b')
Grafo.add_edge(vertices[11],vertices[13], weight=pesos[11], color='b')


Grafo.add_edge(vertices[7],vertices[9], weight=pesos[12], color='b')
Grafo.add_edge(vertices[9],vertices[10], weight=pesos[13], color='b')
Grafo.add_edge(vertices[10],vertices[11], weight=pesos[14], color='b')


Grafo.add_edge(vertices[0],vertices[12], weight=1, color='b')
Grafo.add_edge(vertices[12],vertices[13], weight=pesos[15], color='b')

#"""
#Matriz de adyacencia

        #0          1          2            3           4          5          6         7           8         9         10          11        12            13
mat =  [[0,         1,          pesos[2],  0,           0,         pesos[6],  0,        1,          0,        0,        0,          0,        1,            0        ], #0
        [1,         0,          0,         0,           0,         0,         0,        0,          0,        0,        0,          0,        0,            pesos[1] ], #1
        [pesos[2],  0,          0,         pesos[3],    0,         0,         0,        0,          0,        0,        0,          0,        0,            0        ], #2
        [0,         0,          pesos[3],  0,           pesos[4],  0,         0,        0,          0,        0,        0,          0,        0,            0        ], #3
        [0,         0,          0,         pesos[4],    0,         0,         0,        0,          0,        0,        0,          0,        0,            pesos[5] ], #4
        [pesos[6],  0,          0,         0,           0,         0,         pesos[7], 0,          0,        0,        0,          0,        0,            0        ], #5
        [0,         0,          0,         0,           0,         pesos[7],  0,        0,          0,        0,        0,          0,        0,            pesos[8] ], #6
        [1,         0,          0,         0,           0,         0,         0,        0,          pesos[9], pesos[12],0,          0,        0,            0        ], #7
        [0,         0,          0,         0,           0,         0,         0,        pesos[9],   0,        0,        0,          pesos[10],0,            0        ], #8
        [0,         0,          0,         0,           0,         0,         0,        pesos[12],  0,        0,        pesos[13],  0,        0,            0        ], #9
        [0,         0,          0,         0,           0,         0,         0,        0,          0,        pesos[13],0,          pesos[14],0,            0        ], #10
        [0,         0,          0,         0,           0,         0,         0,        0,          pesos[10],0,        pesos[14],  0,        0,            pesos[11]], #11
        [1,         0,          0,         0,           0,         0,         0,        0,          0,        0,        0,          0,        0,            pesos[15]], #12
        [0,         pesos[1],   0,         0,           pesos[5],  0,         pesos[8], 0,          0,        0,        0,          pesos[13],pesos[15],    0       ]]  #13


def dijkstra(m, inicio, fin):
    tam = len(m)
    dist = [math.inf]*tam
    dist[inicio] = m[inicio][inicio]
    vertice = [False]*tam
    npadre = [-1]*tam
    cami = [{}]*tam
    for i in range(tam-1):
        minix = math.inf
        x = 0
        for y in range(len(vertice)):
            if vertice[y] == False and dist[y] <= minix:
                minix = dist[y]
                x = y

        vertice[x] = True
        
        for y in range(tam):
            if not(vertice[y]) and m[x][y]!=0 and dist[x] + m[x][y] < dist[y]:
                npadre[y] = x
                dist[y] = dist[x] + m[x][y]

    for i in range(tam):
        cont = i
        temp = []
        
        while npadre[cont] != -1:
            temp.append(cont)
            cont = npadre[cont]
            
        temp.append(inicio)
        cami[i] = temp[::-1]
        
    return (dist[fin], cami[fin]) if fin >= 0 else (dist, cami)


pesofin,camino= dijkstra(mat, 0, 13)

for i in range(len(camino)-1):
    Grafo.add_edges_from ([(vertices[camino[i]],vertices[camino[i+1]])], color = 'red')

#"""
"""
#networkx

#camino = nx.dijkstra_path(Grafo, source='U', target = 'I', weight = True) 
length,camino=nx.bidirectional_dijkstra(Grafo,'Casa','CETI') #Siempre usar bidirectional_dijkstra
print(camino)


for i in range(len(camino)-1):
    Grafo.add_edges_from ([(camino[i],camino[i+1])], color = 'red')
""" 

colors = nx.get_edge_attributes(Grafo,'color').values()

coords = {"Casa":(-5,0),"Auto":(0,5),"C85-A":(-2,1.5),"T18-A":(0,2.5),"Providencia":(2,1.5),"C135":(-1.2,0),"Americas":(1.2,0),"R.Center":(-2.5,-1),"C54":(0,-1.5),"C72":(-1,-2.8),"T08":(1,-2.8),"N.Escocia":(2.5,-1),"Bicicleta":(0,-5),"CETI":(5,0)}


nx.draw(
    Grafo, pos= coords, edge_color=colors, width=2, linewidths=2,
    node_size=1500, node_color='pink', alpha=1,
    labels={node: node for node in Grafo.nodes()}
)

nx.draw_networkx_edge_labels(
    Grafo, pos= coords,
    edge_labels={(vertices[0],vertices[1]): 1,
                 (vertices[1],vertices[13]): pesos[1], 
                 
                 (vertices[0],vertices[2]): pesos[2],
                 (vertices[2],vertices[3]): pesos[3],
                 (vertices[3],vertices[4]): pesos[4],
                 (vertices[4],vertices[13]):pesos[5],
                 
                 
                 (vertices[0],vertices[5]): pesos[6],
                 (vertices[5],vertices[6]): pesos[7], 
                 (vertices[6],vertices[13]):pesos[8],
                 
                 
                 (vertices[0],vertices[7]):   1,
                 (vertices[7],vertices[8]):   pesos[9],
                 (vertices[8],vertices[11]):  pesos[10],
                 (vertices[11],vertices[13]): pesos[11],
                 
                 (vertices[7],vertices[9]):   pesos[12], 
                 (vertices[9],vertices[10]):  pesos[13], 
                 (vertices[10],vertices[11]): pesos[14],
                 
                 (vertices[0],vertices[12]):  1,
                 (vertices[12],vertices[13]): pesos[15],
                 
                 },
    font_color='red'
)

for n in camino:
    print(vertices[n])

print("Peso minimo: ",pesofin)
