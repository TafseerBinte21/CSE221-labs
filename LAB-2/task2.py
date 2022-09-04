def selectionSort(a,n,m):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        a[i],a[min]=a[min],a[i]

    string = ""
    for i in range(m):
        string += str(a[i])
        if i != m-1:
            string += " "
    return string



nm = None
array = None
with open('input2.txt') as inFile:
    nm = inFile.readline().split()
    array = inFile.readline().split()


for i in range(len(array)): 
    array[i] = int(array[i])
output=selectionSort(array,int(nm[0]),int(nm[1]))

o = open("output2.txt", 'w')
o.write(output)
o.close()