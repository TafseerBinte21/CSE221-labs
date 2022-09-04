graph={}
with open('input.txt') as inFile:
    count = 0
    
    while True:
        count += 1
        line = inFile.readline()
    
        if not line:
            break
        line = line.split()
        line=list(map(int, line))
        if count!= 1:
            graph.setdefault(line[0] , line[1:])
            
print(graph)
visited =[]
queue = []
def bfs(visited,graph,node,endpoint):
    visited.append(node)
    queue.append(node)
    print('places:', end=" ",file = f)
    while queue!= None:
        m = queue.pop(0)
        print(m,end=" ",file = f)
        if m==endpoint:
            break
        for neighbour in graph.get(m):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

f = open("output2.txt", 'w')
output = bfs(visited,graph,1,12)
f.close()
