#In[0]
from queue import PriorityQueue
import numpy as np
map = np.loadtxt("Day15/input15.txt", str)
length = len(map)

#In[1]


#In[]

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        #self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

def Part_1():
    g1 = Graph(10000)
    for y in range(0, length):
        for x in range(0, length):
            adj = [(y+1, x), (y, x+1), (y, x-1), (y-1, x)]
            for i, j in adj:
                if i in range(length) and j in range(length):
                    g1.add_edge((y*100)+x, (i*100)+j, int(map[i][j]))

    D1 = dijkstra(g1, 0)
    print(D1[9999])
#In[]
def Part_2():
    g2 = Graph(250000)
    for a in range(0, 5):
        for b in range(0, 5):
            for y in range(0, length):
                for x in range(0, length):
                    adj = [(y+1, x), (y, x+1), (y, x-1), (y-1, x)]
                    for i, j in adj:
                        if i in range(length) and j in range(length):
                            if int(map[i][j]) + a + b > 9:
                                if (int(map[i][j]) + a + b)%9 == 0:
                                    g2.add_edge(((a*5000)+(y*500) + (100*b) + x), ((a*5000)+(i*500)+(100*b)+x), 9)
                                else:
                                    g2.add_edge(((a*5000)+(y*500) + (100*b) + x), ((a*5000)+(i*500)+(100*b)+x), (int(map[i][j])+a+b)%9)
                            else:
                                g2.add_edge(((a*5000)+(y*500) + (100*b) + x), ((a*5000)+(i*500)+(100*b)+x), int(map[i][j])+a+b)
    return g2
#In[]
G2 = dijkstra(Part_2(), 0)
print(G2[249999])

# %%
