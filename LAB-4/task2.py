import heapq
import sys

def dijkstra(graph,source):
    
    dist = [sys.maxsize] * (len(graph)+1)
    dist[source] = 0
    priorityQueue = []
    visited = [False] * (len(graph)+1)
    previous = [None] * (len(graph)+1)
    for v in graph:
        if v!= source:
            dist[v] = float('inf')
            previous[v] = None
        heapq.heappush(priorityQueue,[dist[v],v])
    
    while priorityQueue:
        u = heapq.heappop(priorityQueue)
        u = u[1]
        if visited[u]:
            continue
        visited[u] = True
        
        for v in graph[u]:
            alt = dist[u]+graph[u][v]
            if dist[v] > alt:
                dist[v] = alt
                previous[v] = u
                heapq.heappush(priorityQueue,[dist[v],v])
    
    Index = len(graph)
    arr = []
    while Index!=1:
        Index = previous[Index]
        arr.append(Index)
    arr = arr[::-1]
    arr.append(len(graph))
    minimum = " "
    for i in arr:
        minimum+=str(i)+" "
  
    print(minimum,file=o)
    #print(arr)
    return minimum

   
graph={}
c = 1
o = open("output2.txt","w")

with open('input1.txt') as inFile:
    while True:
        line = int(inFile.readline())
        for i in range(line):
            edge = inFile.readline().split()
            vertex = int(edge[0])
            weight = int(edge[1])
            for i in range(1,1+vertex):
                graph[i] = {}
            for j in range(1,1+weight):
                temp = inFile.readline()
                temp = temp.split('\n')
                temp = temp[0].split()
                graph[int(temp[0])][int(temp[1])] = int(temp[2])
            c+=1
            x = dijkstra(graph,1)
        if c > line:
            break
o.close