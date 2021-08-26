n=7
b=[0, 0, 1, 0, 0, 1, 0]
#n=int(input())
#c=list(map(int,input().split()))
def count(target,lst):
    if target==0:
        return [[0]]
    elif lst[target]==1 or target<0:
        return False
    res=[]
    sways=count(target-1,lst)
    #print(sways)
    if sways:
        tways=[[target]+j for j in sways]
        res+=tways
    sways2=count(target-2,lst)
    if sways2:
        tways2=[[target]+j for j in sways2]
        res+=tways2
    return res
a=count(n-1,b)
print(a)
print(len(min(a))-1)
