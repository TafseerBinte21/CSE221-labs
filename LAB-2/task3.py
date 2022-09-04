def insertionSort(array,barray):
    for i in  range(1,len(array)):
        sort = array[i]
        

        while array[i-1] < sort and i>0 :
           array[i],array[i-1]= array[i-1],array[i]
           barray[i],barray[i-1]= barray[i-1],barray[i]
           i-=1
           
    return barray


with open('input3.txt') as inFile:
    n=inFile.readline()
    array=inFile.readline().strip().split(" ")
    barray=inFile.readline().strip().split(" ")
    
   
for i in range(len(array)):
    array[i] = int(array[i])
    for j in range(len(barray)):
        barray[j] = int(barray[j])
out = insertionSort(barray,array)

o = open("output3.txt" , "w")
for i in range(len(out)):
    if i== len(out)-1:
        print(out[i],end=" ",file = o)
    else:
        print(out[i],end=" ",file = o)


o.close()
