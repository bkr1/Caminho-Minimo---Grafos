import os
import time

def minimo(dist, q):
    mini = 10000000
    u = -1
    for i in q:
        if dist[i] < mini:
            mini = dist[i]
            u = i
    return u

def dijkstra(matAdj, s):
    tempoInicio = time.time()

    dist = []
    pred = []
    q = []
    for v in range(len(matAdj)):
        dist.append(5000000)
        pred.append(-1)
        q.append(v) # Q <- V
    
    dist[s] = 0
    while len(q) != 0:
        u = minimo(dist, q)
        q.remove(u)
        for v in range(len(matAdj)):
            if matAdj[u][v] != 0 and dist[v] > (dist[u] + matAdj[u][v]):
                dist[v] = dist[u] + matAdj[u][v]
                pred[v] = u
    
    print("\nDistancias = ")
    print(dist)
    print("\nPredecessores = ")
    print(pred)

    tempoFinal = time.time()
    tempo = tempoFinal - tempoInicio
    print("Tempo de execucao: " + str(tempo) + " s")
    print("\nCusto para o vertice 18: " + str(dist[18]))

    return pred

def bellmanford(matAdj, arestas, s):
    dist = []
    pred = []
    tempoInicio = time.time()

    for v in range(len(matAdj)):
        dist.append(5000000)
        pred.append(-1)
    dist[s] = 0

    for i in range(len(matAdj)):
        for e in arestas:
            if dist[e[1]] > (dist[e[0]] + matAdj[e[0]][e[1]]):
                dist[e[1]] = (dist[e[0]] + matAdj[e[0]][e[1]])
                pred[e[1]] = e[0]

    for e in arestas:
        if dist[e[1]] > (dist[e[0]] + matAdj[e[0]][e[1]]):
            return False

    print("\nDistancias = ")
    print(dist)
    print("\nPredecessores = ")
    print(pred)

    tempoFinal = time.time()
    tempo = tempoFinal - tempoInicio
    print("Tempo de execucao: " + str(tempo) + " s")
    print("\nCusto para o vertice 18: " + str(dist[18]))

    return pred

def floydwarshall(matAdj):
    tempoInicio = time.time()

    dist = [[0 for x in range(len(matAdj))] for x in range(len(matAdj))]
    pred = [[-1 for x in range(len(matAdj))] for x in range(len(matAdj))]

    for i in range(len(matAdj)):
        for j in range(len(matAdj)):
            if i == j:
                dist[i][j] = 0
            elif matAdj[i][j] != 0:
                dist[i][j] = matAdj[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = 5000000
                pred[i][j] = -1

    for k in range(len(matAdj)):
        for i in range(len(matAdj)):
            for j in range(len(matAdj)):
                if dist[i][j] > (dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    print("\nDistancias = ")
    for i in range(len(dist)):
       print(dist[i])
    print("\nPredecessores = ")
    for i in range(len(pred)):
       print(pred[i])

    tempoFinal = time.time()
    tempo = tempoFinal - tempoInicio
    print("\nTempo de execucao: " + str(tempo) + " s")
    print("\nCusto para o vertice 18: " + str(dist[0][18]))

    return pred
