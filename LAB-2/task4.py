import math
def merge(array, leftIndex, rightIndex,mid):
    n1 = mid - leftIndex+ 1
    n2 = rightIndex- mid
    l = []
    r = []
    for i in range(1,n1+1):
        
        l.append(array[leftIndex+i-1])
    for j in range(1,n2+1):
      
        r.append(array[mid+j])
    
    l.append(math.inf)
    r.append(math.inf)
    
    i = 0
    j = 0
    k = 0
   
    for k in range(leftIndex,rightIndex+1):
            if r[j] > l[i]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1


def mergeSort(array,leftIndex,rightIndex):
    if leftIndex< rightIndex:
        

        mid = (leftIndex+rightIndex)//2
        mergeSort(array,leftIndex,mid)
        mergeSort(array,mid+1,rightIndex)
        merge(array,leftIndex,rightIndex,mid)




with open('input4.txt') as inFile:
    n=inFile.readline()
    array=inFile.readline().strip().split(" ")
    
    
    
for i in range(len(array)):
    array[i] = int(array[i])
mergeSort(array,0,len(array)-1)
out = array

o = open("output4.txt" , "w")
for i in range(len(out)):
    if i== len(out)-1:
        print(out[i],end=" ",file = o)
    else:
        print(out[i],end=" ",file = o)


o.close()