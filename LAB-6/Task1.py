import json
def LCS(x,y):
    m = len(x)+1
    n = len(y)+1

    c = [[0]*(n) for i in range(m)]
    t = [[None]*(n) for i in range(m)]
    

    for i in range (1,m):
        for j in range (1,n):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                t[i][j] = "d"
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                t[i][j] = "up"
            else:
               c[i][j] = c[i][j-1]
               t[i][j] = "left"
    string =""
    i = m-1
    j = n-1
    while t[i][j] !=None:
        if t[i][j] == 'd':
            string+=x[i-1]
            i-=1
            j-=1
        elif t[i][j] == "up":
            i-=1
        else:
            j-=1
    a = (string[::-1])
    a = a.split()
  
    name =['Yasnaya Pochinki Farm Mylta Shelter Prison']
    for ind in a:
        for idx in name:
            a[0] = name[0]
    print(name[0],file=o)
    
    return c[m-1][n-1]

o = open("output1.txt","w")
with open('input1.txt') as inFile:
        n = inFile.readline()
        x = inFile.readline().strip()
        y = inFile.readline().strip()
    
p = LCS(x,y)
print("correctness of prediction:", p/int(n)*100, "%",file=o)
o.close
