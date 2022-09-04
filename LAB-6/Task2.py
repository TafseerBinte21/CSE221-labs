def LCS(x,y,z):
    m = len(x)+1
    n = len(y)+1
    o = len(z)+1
 
   
    c = [[[0]*(o) for k in range(n)] for j in range(m)]
    t = [[[None]*(o) for k in range(n)] for j in range(m)]

    for i in range (1,m):
       for j in range (1,n):
           for k in range(1,o):
               if i == 0 or j == 0 or k == 0:
                   t [i][j][k] = None
               else:
                    if x[i-1] == y[j-1] and x[i-1]== z[k-1]:
                            c[i][j][k] = 1+c[i-1][j-1][k-1]
                            t[i][j][k] = 'd'
                    else:
                        if c[i-1][j][k] >= c[i][j-1][k]:
                            max = c[i-1][j][k]
                            if max >= c[i][j][k-1]:
                                c[i][j][k] = max
                                t[i][j][k] = 'up-up-Left'
                            else:
                                max = c[i][j][k-1]
                                c[i][j][k] = max
                                t[i][j][k] = 'Left-up-up'
                        else:
                            max = c[i][j-1][k]
                            if max >= c[i][j][k-1]:
                                c[i][j][k] = max
                                t[i][j][k] = 'up-Left-up'
                            else:
                                max = c[i][j][k-1]
                                c[i][j][k] = max
                                t[i][j][k] = 'Left-up-up'

   

    
    return c[m-1][n-1][o-1]

ot = open("output2.txt","w")
with open('input2.txt') as inFile:
        x = inFile.readline().strip()
        y = inFile.readline().strip()
        z = inFile.readline().strip()
        
p = LCS(x,y,z)
print(p,file=ot)
ot.close
   