import os
import CaminhoMinimo as func

def mainf():
    os.system("cls")
    print("\t------- CAMINHO MINIMO -------\n\n")

    op = 0
    while op == 0:
        print("\t1    Usar grafo de teste;" + "\n\t2    Inserir grafo;\n")
        op = int(input("\nDigite sua opcao: "))

    if op == 1:
        file = open("grafo01.txt")
    elif op == 2:
        fileName = input("\nDigite o nome do arquivo .txt: ")
        file = open(fileName)

    #Definir o numero de vertices e arestas do grafo:
    str = file.readline()
    str = str.split(" ")

    numVertices = int(str[0])
    numArestas = int(str[1])

    #Preencher uma Lista de Adjacencias e uma Matriz de Adjacencias vazias:
    listaAdj = [[]for x in range(numVertices)]
    matAdj = [[0 for x in range(numVertices)] for x in range(numVertices)]

    #vertices = [x for x in range(numVertices)]
    arestas = []

    #Preencher as estruturas com as devidas adjacencias:
    for i in range(numArestas):
        str = file.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        listaAdj[origem].append((destino, peso))
        matAdj[origem][destino] = peso
        arestas.append((origem, destino, peso))

    #print("\nLista de Adjacencias: \n")
    #print(listaAdj)

    #print("\nMatriz de Adjacencias: \n")

    #for i in range(len(matAdj)):
        #print(matAdj[i])
    os.system("pause")
    os.system("cls")

    op = 0
    while op != 4:
        if op != 4:
            print("\t------- CAMINHO MINIMO -------\n\n")
            print("\n\t1    Algoritmo de Dijkstra;" + "\n\t2    Algoritmo de Bellman - Ford;" +
                  "\n\t3    Algoritmo de Floyd - Warshall;" + "\n\t4    Sair.")
            op = int(input("\nInforme sua opcao: "))

            if op == 1:
                os.system("cls")
                origem = int(input("Informe o vertice de partida: "))
                destino = int(input("Informe o vertice destino: "))
                print("\nProcessando...")
                pred = func.dijkstra(matAdj, origem)

                caminho = []
                caminho.append(destino)

                while caminho[0] != origem:
                    caminho.insert(0, pred[destino])
                    destino = pred[destino]

                print("\nCaminho: ")
                print(caminho)

                os.system("pause")
                os.system("cls")
            elif op == 2:
                os.system("cls")
                origem = int(input("Informe o vertice de partida: "))
                destino = int(input("Informe o vertice destino: "))
                print("\nProcessando...")
                pred = func.bellmanford(matAdj, arestas, origem)

                caminho = []
                caminho.append(destino)

                while caminho[0] != origem:
                    caminho.insert(0, pred[destino])
                    destino = pred[destino]
                
                print("\nCaminho: ")
                print(caminho)

                os.system("pause")
                os.system("cls")

            elif op == 3:
                os.system("cls")

                origem = int(input("Informe a origem: "))
                destino = int(input("Informe o destino: "))
                print("\nProcessando...")
                pred = func.floydwarshall(matAdj)
                caminho = []
                caminho.append(destino)

                while caminho[0] != origem:
                    caminho.insert(0, pred[origem][destino])
                    destino = pred[origem][destino]

                print("\nCaminho: ")
                print(caminho)
                os.system("pause")
                os.system("cls")


mainf()
os.system("cls")