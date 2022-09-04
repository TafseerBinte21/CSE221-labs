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
    
    l.append([0,math.inf])
    r.append([0,math.inf])
    
    i = 0
    j = 0
    k = 0
   
    for k in range(leftIndex,rightIndex+1):
            if r[j][1] > l[i][1]:
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

def assignment_selection(a,n):
    count = 1
    selected =[a[0]]
    finishing = a[0][1]
    for i in range(1,n):
            if a[i][0] >= finishing:
                count+=1
                finishing = a[i][1]
                selected.append(a[i])
                
    string=""
    for i in range(len(selected)):
        string+=str(selected[i][0]) + " " + str(selected[i][1])+"\n"
    print(count,file=o)
    print(string,file=o)

o = open("output1.txt","w")
with open('task1_input.txt') as inFile:
    n=int(inFile.readline())
    array = []
    while n!=0:
        se=inFile.readline().split()
        se[0] , se[1] = int(se[0]) , int(se[1])
        array.append(se)
        n-=1

mergeSort(array,0,len(array)-1)
assignment_selection(array,len(array))
o.close