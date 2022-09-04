def bubbleSort(a):


    swap = True
    while swap:
           
        swap = False
        for i in range (0,len(a)-1):
            
            if a[i]> a[i+1]:
                swap = True
                a[i],a[i+1] = a[i+1],a[i]
            
            if swap == True:
              break
        
    return a         

#We have reduced the time complexity by taking a flag variable to stop the bubble sort as soon as it becomes sorted.
#and this is how we can reduce time complexity to O(n)

#taking input 
with open('input1.txt') as inFile:
    n = inFile.readline()
    a = inFile.readline().split()
    
for i in range(len(a)):
    a[i] = int(a[i])

out = bubbleSort(a)

o = open("output1.txt" , "w")
for i in range(len(out)):
    if i== len(out)-1:
        print(out[i],end=" ",file = o)
    else:
        print(out[i],end=" ",file = o)

o.close()



