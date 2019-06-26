from queue import Queue
from collections import defaultdict
import sys

##Used the same thought process from https://www.geeksforgeeks.org/longest-path-directed-acyclic-graph-set-2/
##to help solve this assignment. 

def longest_path(graph, vertexNum):
    #initializing matrix
    matrix = {}
    for i in range(1, vertexNum+1):
        matrix[i] = [0, 0]

    #uses a queue to help get and store items
    q = Queue()
    q.put(1)

    #helps keep track of nodes we have already visited 
    checkedNodes = []
    checkedNodes.append(1)
    matrix[1][1] = 1
    
    while q.empty() is not True:
        vertex1 = q.get()
        if vertex1 == vertexNum:
            continue
        for vertex2, weight in graph[vertex1].items():
            if vertex2 not in checkedNodes:
                checkedNodes.append(vertex2)
                q.put(vertex2)
            if matrix[vertex1][0] + weight > matrix[vertex2][0]:
                matrix[vertex2][1] = 0
                matrix[vertex2][0] = matrix[vertex1][0] + weight
                matrix[vertex2][1] += matrix[vertex1][1]  
            elif matrix[vertex1][0] + weight == matrix[vertex2][0]:
                matrix[vertex2][1] += matrix[vertex1][1]
    
    print("longest path: {}".format(matrix[vertexNum][0]))
    print("number of longest paths: {}".format(matrix[vertexNum][1]))
    return 


def main():
    #This reads in the number of verticies and edges from the first line of the .txt file
    reader = (sys.stdin.readline().strip()).split(" ")
    
    vertex = reader[0]
    edge = reader[1]

    #This initiliazes an empty graph "graph" based off of the # of verticies
    graph = {}
    for i in range(1, int(vertex) + 1):
        graph[i] = {}

    #Iterates through .txt file based off of number of edges
    for i in range(int(edge)):
        graphInfo = sys.stdin.readline().strip().split()
        graph[int(graphInfo[0])][int(graphInfo[1])] = int(graphInfo[2])
    
    #Finds the longest path as well as helps find the # of longest paths
    longest_path(graph, int(vertex))



if __name__ == "__main__":
    main()
