def matrixMultiplication(A, B):

    C = [[0]*(len(A)) for k in range(len(B[0]))]

    for i in range(len(A)):

        for j in range(len(B[0])):

            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


A = []
B = []
with open("input4.txt") as inFile:
    n = int(inFile.readline())
    for i in range(n*2+1):
        aline = inFile.readline().split('\n')
        aline = aline[0]
        if (i < n):
            arr = aline.split(' ')
            A.append(list(map(int, arr)))
        elif(i > n):
            arr = aline.split(' ')
            B.append(list(map(int, arr)))



C = matrixMultiplication(A, B)
with open("output4.txt", "w") as outFile:
    for i in C:
        for j in i:
            print(j, end=' ', file=outFile)
        print('\n', end='', file=outFile)
