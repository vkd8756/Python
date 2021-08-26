def cansum(target,lst):
    l=[False]*(target+1)
    l[0]=True
    i=0
    while i<=target:
        if l[i]==True:
            for num in lst:
                if i+num<=target:
                    l[i+num]=True
        i+=1
        #print(l)
    return l[target]

print(cansum(7,[5,4,3]))

def howsum(target,lst):
    l=[0]*(target+1)
    l[0]=[]
    i=0
    while i<=target:
        if l[i] != 0:
            for num in lst:
                if i+num<=target:
                    l[i+num]=l[i]+[num]
        i+=1
        print(l)
    return l[target]
print("\n",howsum(7,[5,4,3]))
print(howsum(7,[2,3]))
