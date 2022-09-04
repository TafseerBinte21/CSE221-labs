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
            
print("the graph is:")   
for i,j in graph.items():
        print(i,":",j)
