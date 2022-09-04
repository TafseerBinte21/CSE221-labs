
def activities(tasks,call):
    sequence = []
    jackhours = 0
    jillhours = 0
    jack = []
    jill = []

    for c in call:
        if c == 'J':
            jack.append(min(tasks))
            sequence.append(str(min(tasks)))
            jackhours+=min(tasks)
            tasks.remove(min(tasks))
        else:
            if c == 'j':
                jill.append(max(jack))
                jillhours+=max(jack)
                sequence.append(str(max(jack)))
                jack.remove(max(jack))

    
    s =""
    for i in sequence:
        s+=str(i)
    print(s,file=o)

    print("Jack will work for"+ " "+ str(jackhours)+ " " +"hours",file=o)
    print("Jack will work for"+ " "+ str(jillhours)+ " " +"hours",file=o)

o = open("output3.txt","w")
with open('task3_input.txt') as inFile:
    n=int(inFile.readline())
    h = inFile.readline().split()
    for j in range(len(h)):
        h[j] = int(h[j])  
    call = inFile.readline()
    
activities(h,call)
o.close
        