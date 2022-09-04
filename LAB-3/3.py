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

visited = []
def dfs_visit(graph,node):
    for i in graph[node]:
        if i not in visited:
            visited.append(i)
            dfs_visit(graph,i)

def dfs(grap,endpoint):
    for i in [*graph]:
        if i not in visited:
            visited.append(i)
            dfs_visit(graph,i)
    
    
f = open("output3.txt",'w')
print('places:',end=" ",file = f)
dfs(graph,'12')
for j in visited:
    print(j,end = ' ',file=f)
    if j == 12:
        break
f.close()
