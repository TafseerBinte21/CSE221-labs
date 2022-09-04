import heapq
import sys

def network(graph,source):
    
    dist = [sys.maxsize*(-1)] * (len(graph)+1)
    dist[source] = float('inf')
    priorityQueue = []
    visited = [False] * (len(graph)+1)
    previous = [None] * (len(graph)+1)
    for v in graph:
        if v!= source:
            dist[v] = sys.maxsize*(-1)
            previous[v] = None
        heapq.heappush(priorityQueue,[dist[v]*(-1),v])
    
    while priorityQueue:
        u = heapq.heappop(priorityQueue)
        u = u[1]
        if visited[u]:
            continue
        visited[u] = True
        
        for v in graph[u]:
            alt = min(dist[u],graph[u][v])
            if dist[v] < alt:
                dist[v] = alt
                previous[v] = u
                heapq.heappush(priorityQueue,[dist[v]*(-1),v])
    for i in range(len(dist)):
        if dist[i] == (-1)*sys.maxsize: 
            dist[i]=-1
        if dist[i] == float('inf'): 
            dist[i]=0
    
    return dist[1:]

   
graph={}
c = 1
o = open("output4.txt","w")
with open('input4.txt') as inFile:
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
            src = int(inFile.readline())
            c+=1
            x = network(graph,src)
            string=" "
            for i in x:
                string+=str(i)+" "
            print(string,file=o)
        if c > line:
            break
o.close